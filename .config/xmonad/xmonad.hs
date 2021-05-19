-- Data
import Data.Monoid
import Data.Tree
import System.Exit (exitSuccess)
import System.IO (hPutStrLn)
import XMonad
import XMonad.Actions.CopyWindow (kill1)
import XMonad.Actions.CycleWS (nextScreen, prevScreen)
import XMonad.Actions.MouseResize
import XMonad.Actions.WithAll (sinkAll)
import XMonad.Actions.UpdatePointer

-- Hooks
import XMonad.Hooks.DynamicLog (PP (..), dynamicLogWithPP, shorten, wrap, xmobarColor, xmobarPP)
import XMonad.Hooks.EwmhDesktops
import XMonad.Hooks.FadeInactive
import XMonad.Hooks.ManageDocks (ToggleStruts (..), avoidStruts, docksEventHook, manageDocks)
import XMonad.Hooks.ManageHelpers (doFullFloat, isFullscreen)
import XMonad.Hooks.SetWMName
import XMonad.Hooks.WorkspaceHistory
import XMonad.Hooks.InsertPosition

-- Layouts
import XMonad.Layout.GridVariants (Grid (Grid))
import XMonad.Layout.LayoutModifier
import XMonad.Layout.LimitWindows (limitWindows)
import XMonad.Layout.MultiToggle ((??), EOT (EOT), mkToggle, single)
import qualified XMonad.Layout.MultiToggle as MT (Toggle (..))
import XMonad.Layout.MultiToggle.Instances (StdTransformers (MIRROR, NBFULL, NOBORDERS))
import XMonad.Layout.NoBorders
import XMonad.Layout.Renamed (Rename (Replace), renamed)
import XMonad.Layout.ResizableTile
import XMonad.Layout.ShowWName
import XMonad.Layout.SimplestFloat
import XMonad.Layout.Spacing
import XMonad.Layout.ThreeColumns
import qualified XMonad.Layout.ToggleLayouts as T (ToggleLayout (Toggle), toggleLayouts)
import XMonad.Layout.WindowArranger (WindowArrangerMsg (..), windowArrange)
import qualified XMonad.StackSet as W

-- Utilities
import XMonad.Util.EZConfig (additionalKeysP)
import XMonad.Util.Run (spawnPipe)
import XMonad.Util.SpawnOnce

myModMask = mod4Mask :: KeyMask

myTerminal = "alacritty" :: String

myBorderWidth = 1 :: Dimension

myNormColor = "#292d3e" :: String

myFocusColor = "#c792ea" :: String

windowCount :: X (Maybe String)
windowCount = gets $ Just . show . length . W.integrate' . W.stack . W.workspace . W.current . windowset

myStartupHook :: X ()
myStartupHook = do
    spawnOnce "trayer --edge top  --monitor 1 --widthtype pixel --width 40 --heighttype pixel --height 18 --align right --transparent true --alpha 0 --tint 0x292d3e --iconspacing 3 --distance 1 &"
    setWMName "LG3D"


mySpacing :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
mySpacing i = spacingRaw False (Border i i i i) True (Border i i i i) True

-- Single window with no gaps
mySpacing' :: Integer -> l a -> XMonad.Layout.LayoutModifier.ModifiedLayout Spacing l a
mySpacing' i = spacingRaw True (Border i i i i) True (Border i i i i) True

-- Layouts definition

tall = renamed [Replace "tall"]
    $ limitWindows 12
    $ mySpacing 4
    $ ResizableTall 1 (3 / 100) (1 / 2) []

monocle = renamed [Replace "monocle"] $ limitWindows 20 Full

grid = renamed [Replace "grid"]
    $ limitWindows 12
    $ mySpacing 4
    $ mkToggle (single MIRROR)
    $ Grid (16 / 10)

threeCol = renamed [Replace "threeCol"]
    $ limitWindows 7
    $ mySpacing' 4
    $ ThreeCol 1 (3 / 100) (1 / 3)

floats = renamed [Replace "floats"] $ limitWindows 20 simplestFloat

-- Layout hook

myLayoutHook = avoidStruts 
    $ smartBorders
    $ mouseResize
    $ windowArrange
    $ T.toggleLayouts floats
    $ mkToggle (NBFULL ?? NOBORDERS ?? EOT) myDefaultLayout
  where
    myDefaultLayout = 
        noBorders monocle
        ||| tall
        ||| threeCol
        ||| grid

xmobarEscape :: String -> String
xmobarEscape = concatMap doubleLts
  where
    doubleLts '<' = "<<"
    doubleLts x = [x]

myWorkspaces :: [String]
myWorkspaces = clickable . (map xmobarEscape)
--                                                                                            
--    $ ["\xf269 ", "\xe61f ", "\xe795 ", "\xf121 ", "\xf419 ", "\xf308 ", "\xf74a ", "\xf7e8 ", "\xf827 "]
    $ ["www", "dev", "term", "ref", "git", "dock", "fs", "media", "misc"]
  where
    clickable l = ["<action=xdotool key super+" ++ show (i) ++ "> " ++ ws ++ "</action>" | (i, ws) <- zip [1 .. 9] l]

myKeys :: [(String, X ())]
myKeys = 
    [
    ------------------ Window configs ------------------

    -- Move focus to the next window
    ("M-j", windows W.focusDown),
    -- Move focus to the previous window
    ("M-k", windows W.focusUp),
    -- Swap focused window with next window
    ("M-S-j", windows W.swapDown),
    -- Swap focused window with prev window
    ("M-S-k", windows W.swapUp),
    -- Kill window
    ("M-w", kill1),
    -- Restart xmonad
    ("M-C-r", spawn "xmonad --restart"),
    -- Quit xmonad
    ("M-C-q", io exitSuccess),

    ----------------- Floating windows -----------------

    -- Toggles 'floats' layout
    ("M-f", sendMessage (T.Toggle "floats")),
    -- Push floating window back to tile
    ("M-S-f", withFocused $ windows . W.sink),
    -- Push all floating windows to tile
    ("M-C-f", sinkAll),

    ---------------------- Layouts ----------------------

    -- Switch focus to next monitor
    ("M-.", nextScreen),
    -- Switch focus to prev monitor
    ("M-,", prevScreen),
    -- Switch to next layout
    ("M-<Tab>", sendMessage NextLayout),
    -- Switch to first layout
    ("M-S-<Tab>", sendMessage FirstLayout),
    -- Toggles noborder/full
    ("M-<Space>", sendMessage (MT.Toggle NBFULL) >> sendMessage ToggleStruts),
    -- Toggles noborder
    ("M-S-n", sendMessage $ MT.Toggle NOBORDERS),
    -- Shrink horizontal window width
    ("M-S-h", sendMessage Shrink),
    -- Expand horizontal window width
    ("M-S-l", sendMessage Expand),
    -- Shrink vertical window width
    ("M-C-j", sendMessage MirrorShrink),
    -- Exoand vertical window width
    ("M-C-k", sendMessage MirrorExpand),

    -------------------- App configs --------------------

    -- Menu
    ("M-m", spawn "rofi -show drun"),
    -- Window nav
    ("M-S-m", spawn "rofi -show"),
    -- Browser
    ("M-b", spawn "firefox"),
    -- File explorer
    ("M-e", spawn "pcmanfm"),
    -- Terminal
    ("M-<Return>", spawn myTerminal),
    -- Redshift
    ("M-r", spawn "redshift -O 2400"),
    ("M-S-r", spawn "redshift -x"),
    -- Scrot
    ("M-s", spawn "scrot"),
    ("M-S-s", spawn "scrot -s"),

    --------------------- Hardware ---------------------

    -- Volume
    ("<XF86AudioLowerVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ("<XF86AudioRaiseVolume>", spawn "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ("<XF86AudioMute>", spawn "pactl set-sink-mute @DEFAULT_SINK@ toggle" ),

    -- Brightness
    ("<XF86MonBrightnessUp>", spawn "brightnessctl set +10%"),
    ("<XF86MonBrightnessDown>", spawn "brightnessctl set 10%-")
    ]

main :: IO ()
main = do
    -- Xmobar
    xmobarLaptop <- spawnPipe "xmobar -x 0 ~/.config/xmobar/primary.hs"
    xmobarMonitor <- spawnPipe "xmobar -x 1 ~/.config/xmobar/secondary.hs"
    -- Xmonad
    xmonad $ ewmh def {
        manageHook = (isFullscreen --> doFullFloat) <+> manageDocks <+> insertPosition Below Newer,
        handleEventHook = docksEventHook,
        modMask = myModMask,
        terminal = myTerminal,
        startupHook = myStartupHook,
        layoutHook = myLayoutHook,
        workspaces = myWorkspaces,
        borderWidth = myBorderWidth,
        normalBorderColor = myNormColor,
        focusedBorderColor = myFocusColor,
        -- Log hook
        logHook = workspaceHistoryHook <+> dynamicLogWithPP xmobarPP {
            ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor x,
            -- Current workspace in xmobar
            ppCurrent = xmobarColor "#c3e88d" "" . wrap "[" " ]",
            -- Visible but not current workspace
            ppVisible = xmobarColor "#c3e88d" "",
            -- Hidden workspaces in xmobar
            ppHidden = xmobarColor "#82AAFF" "",
            -- Hidden workspaces (no windows)
            ppHiddenNoWindows = xmobarColor "#c792ea" "",
            -- Title of active window in xmobar
            ppTitle = xmobarColor "#6272a4" "" . shorten 55,
            -- Separators in xmobar
            ppSep = "<fc=#666666> | </fc>",
            -- Urgent workspace
            ppUrgent = xmobarColor "#C45500" "" . wrap "" "!",
            -- Number of windows in current workspace
            ppExtras = [windowCount],
            ppOrder = \(ws : l : t : ex) -> [ws, l] ++ ex ++ [t]
        } >> updatePointer (0.5, 0.5) (0.5, 0.5) 
} `additionalKeysP` myKeys
