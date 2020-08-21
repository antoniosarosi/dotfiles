-- Base

-- Actions

-- Data
import Data.Char (isSpace)
import qualified Data.Map as M
import Data.Maybe (isJust)
import Data.Monoid
import Data.Tree
import System.Exit (exitSuccess)
import System.IO (hPutStrLn)
import XMonad
import XMonad.Actions.CopyWindow (kill1, killAllOtherCopies)
import XMonad.Actions.CycleWS (WSType (..), moveTo, nextScreen, prevScreen, shiftTo)
import XMonad.Actions.GridSelect
import XMonad.Actions.MouseResize
import XMonad.Actions.Promote
import XMonad.Actions.RotSlaves (rotAllDown, rotSlavesDown)
import XMonad.Actions.WindowGo (runOrRaise)
import XMonad.Actions.WithAll (killAll, sinkAll)
-- Hooks
import XMonad.Hooks.DynamicLog (PP (..), dynamicLogWithPP, shorten, wrap, xmobarColor, xmobarPP)
import XMonad.Hooks.EwmhDesktops -- for some fullscreen events, also for xcomposite in obs.
import XMonad.Hooks.FadeInactive
import XMonad.Hooks.ManageDocks (ToggleStruts (..), avoidStruts, docksEventHook, manageDocks)
import XMonad.Hooks.ManageHelpers (doFullFloat, isFullscreen)
import XMonad.Hooks.ServerMode
import XMonad.Hooks.SetWMName
import XMonad.Hooks.WorkspaceHistory
-- Layouts
import XMonad.Layout.GridVariants (Grid (Grid))
-- Layouts modifiers
import qualified XMonad.Layout.Fullscreen as LF
import XMonad.Layout.LayoutModifier
import XMonad.Layout.LimitWindows (decreaseLimit, increaseLimit, limitWindows)
import XMonad.Layout.Magnifier
import XMonad.Layout.MultiToggle ((??), EOT (EOT), mkToggle, single)
import qualified XMonad.Layout.MultiToggle as MT (Toggle (..))
import XMonad.Layout.MultiToggle.Instances (StdTransformers (MIRROR, NBFULL, NOBORDERS))
import XMonad.Layout.NoBorders
import XMonad.Layout.Renamed (Rename (Replace), renamed)
import XMonad.Layout.ResizableTile
import XMonad.Layout.ShowWName
import XMonad.Layout.SimplestFloat
import XMonad.Layout.Spacing
import XMonad.Layout.Spiral
import XMonad.Layout.Tabbed
import XMonad.Layout.ThreeColumns
import qualified XMonad.Layout.ToggleLayouts as T (ToggleLayout (Toggle), toggleLayouts)
import XMonad.Layout.WindowArranger (WindowArrangerMsg (..), windowArrange)
import qualified XMonad.StackSet as W
-- Utilities
import XMonad.Util.EZConfig (additionalKeysP)
import XMonad.Util.Run (runProcessWithInput, safeSpawn, spawnPipe)
import XMonad.Util.SpawnOnce

myFont :: String
myFont = "xft:UbuntuMono Nerd Font:bold:size=11:antialias=true:hinting=true"

myModMask :: KeyMask
myModMask = mod4Mask -- Sets modkey to super/windows key

myTerminal :: String
myTerminal = "alacritty" -- Sets default terminal


myBorderWidth :: Dimension
myBorderWidth = 1 -- Sets border width for windows

myNormColor :: String
myNormColor = "#292d3e" -- Border color of normal windows

myFocusColor :: String
myFocusColor = "#bbc5ff" -- Border color of focused windows

windowCount :: X (Maybe String)
windowCount = gets $ Just . show . length . W.integrate' . W.stack . W.workspace . W.current . windowset

myStartupHook :: X ()
myStartupHook = do
    spawnOnce "trayer --edge top  --monitor 1 --widthtype pixel --width 100 --heighttype pixel --height 18 --align right --margin 360 --transparent true --alpha 0 --tint 0x292d3e --iconspacing 3 --distance 1 &"
    setWMName "LG3D"


mySpacing :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
mySpacing i = spacingRaw False (Border i i i i) True (Border i i i i) True

-- Below is a variation of the above except no borders are applied
-- if fewer than two windows. So a single window has no gaps.
mySpacing' :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
mySpacing' i = spacingRaw True (Border i i i i) True (Border i i i i) True

-- Defining a bunch of layouts, many that I don't use.
tall =
  renamed [Replace "tall"]
    $ limitWindows 12
    $ mySpacing 4
    $ ResizableTall 1 (3 / 100) (1 / 2) []

monocle =
  renamed [Replace "monocle"] $
    limitWindows 20 Full

grid =
  renamed [Replace "grid"]
    $ limitWindows 12
    $ mySpacing 4
    $ mkToggle (single MIRROR)
    $ Grid (16 / 10)

threeCol =
  renamed [Replace "threeCol"]
    $ limitWindows 7
    $ mySpacing' 4
    $ ThreeCol 1 (3 / 100) (1 / 3)

floats =
  renamed [Replace "floats"] $
    limitWindows 20 simplestFloat

-- The layout hook
myLayoutHook =
  avoidStruts $ smartBorders $ mouseResize $ windowArrange $ LF.fullscreenFloat $ LF.fullscreenFull $ T.toggleLayouts floats $
    mkToggle (NBFULL ?? NOBORDERS ?? EOT) myDefaultLayout
  where
    -- I've commented out the layouts I don't use.
    myDefaultLayout =
      monocle
        ||| tall
        ||| threeCol
        ||| grid

xmobarEscape :: String -> String
xmobarEscape = concatMap doubleLts
  where
    doubleLts '<' = "<<"
    doubleLts x = [x]

myWorkspaces :: [String]
myWorkspaces =
  clickable . (map xmobarEscape) $
    ["www", "dev", "term", "ref", "sys", "fs", "img", "vid", "misc"]
  where
    clickable l = ["<action=xdotool key super+" ++ show (i) ++ "> " ++ ws ++ "</action>" | (i, ws) <- zip [1 .. 9] l]


myLogHook :: X ()
myLogHook = fadeInactiveLogHook fadeAmount
  where
    fadeAmount = 1.0


myKeys :: [(String, X ())]
myKeys =
  [ ------------------ Window configs ------------------

    -- Move focus to the next window
    ("M-j", windows W.focusDown),
    -- Move focus to the prev window
    ("M-k", windows W.focusUp),
    -- Swap focused window with next window
    ("M-S-j", windows W.swapDown),
    -- Swap focused window with prev window
    ("M-S-k", windows W.swapUp),
    -- Kill the currently focused client
    ("M-w", kill1),
    -- Restarts xmonad
    ("M-C-r", spawn "xmonad --restart"),
    -- Quits xmonad
    ("M-C-q", io exitSuccess),
    ------------------ App configs ------------------

    -- Menu
    ("M-m", spawn "rofi -show run"),
    -- Window nav
    ("M-S-m", spawn "rofi -show"),
    -- Browser
    ("M-b", spawn "firefox"),
    -- File explorer
    ("M-e", spawn "thunar"),
    -- Terminal
    ("M-<Return>", spawn myTerminal),
    -- Redshift
    ("M-r", spawn "redshift -O 2400"),
    ("M-S-r", spawn "redshift -x"),
    -- Floating windows
    -- Toggles my 'floats' layout
    ("M-f", sendMessage (T.Toggle "floats")),
    -- Push floating window back to tile
    ("M-S-f", withFocused $ windows . W.sink),
    -- Push ALL floating windows to tile
    ("M-S-<Delete>", sinkAll),
    -- Layouts
    -- Switch to next layout
    ("M-<Tab>", sendMessage NextLayout),
    ("M-C-M1-<Up>", sendMessage Arrange),
    ("M-C-M1-<Down>", sendMessage DeArrange),
    -- Toggles noborder/full
    ("M-<Space>", sendMessage (MT.Toggle NBFULL) >> sendMessage ToggleStruts),
    -- Toggles struts
    ("M-S-<Space>", sendMessage ToggleStruts),
    -- Toggles noborder
    ("M-S-n", sendMessage $ MT.Toggle NOBORDERS),
    -- Increase number of clients in master pane
    ("M-<KP_Multiply>", sendMessage (IncMasterN 1)),
    -- Decrease number of clients in master pane
    ("M-<KP_Divide>", sendMessage (IncMasterN (-1))),
    -- Increase number of windows
    ("M-S-<KP_Multiply>", increaseLimit),
    -- Decrease number of windows
    ("M-S-<KP_Divide>", decreaseLimit),
    -- Shrink horiz window width
    ("M-h", sendMessage Shrink),
    -- Expand horiz window width
    ("M-l", sendMessage Expand),
    -- Shrink vert window width
    ("M-C-j", sendMessage MirrorShrink),
    -- Exoand vert window width
    ("M-C-k", sendMessage MirrorExpand),
    -- Workspaces
    -- Switch focus to next monitor
    ("M-.", nextScreen),
    -- Switch focus to prev monitor
    ("M-,", prevScreen),
    -- Hardware
    ("<XF86AudioLowerVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ("<XF86AudioRaiseVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ("XF86AudioMute", spawn "pactl set-sink-mute @DEFAULT_SINK@ toggle" ), -- Doesn't work

    ("XF86MonBrightnessUp", spawn "brightnessctl set +10%"), -- Doesn't work
    ("XF86MonBrightnessDown", spawn "brightnessctl set -10%") -- Doesn't work
    ]

main :: IO ()
main = do
  xmobarLaptop <- spawnPipe "xmobar -x 0 ~/.config/xmobar/laptop.hs"
  xmobarMonitor <- spawnPipe "xmobar -x 1 ~/.config/xmobar/monitor.hs"
  xmonad $ ewmh def
        { manageHook = LF.fullscreenManageHook <+> (isFullscreen --> doFullFloat) <+> manageDocks,
          handleEventHook = LF.fullscreenEventHook <+> docksEventHook,
          modMask = myModMask,
          terminal = myTerminal,
          startupHook = myStartupHook,
          layoutHook = myLayoutHook,
          workspaces = myWorkspaces,
          borderWidth = myBorderWidth,
          normalBorderColor = myNormColor,
          focusedBorderColor = myFocusColor,
          logHook = workspaceHistoryHook <+> myLogHook <+> dynamicLogWithPP xmobarPP
                  { ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor x,
                    ppCurrent = xmobarColor "#c3e88d" "" . wrap "[" " ]", -- Current workspace in xmobar
                    ppVisible = xmobarColor "#c3e88d" "", -- Visible but not current workspace
                    ppHidden = xmobarColor "#82AAFF" "", -- Hidden workspaces in xmobar
                    ppHiddenNoWindows = xmobarColor "#c792ea" "", -- Hidden workspaces (no windows)
                    ppTitle = xmobarColor "#b3afc2" "" . shorten 55, -- Title of active window in xmobar
                    ppSep = "<fc=#666666> | </fc>", -- Separators in xmobar
                    ppUrgent = xmobarColor "#C45500" "" . wrap "" "!", -- Urgent workspace
                    ppExtras = [windowCount], -- # of windows current workspace
                    ppOrder = \(ws : l : t : ex) -> [ws, l] ++ ex ++ [t]
                  }
        }
      `additionalKeysP` myKeys
