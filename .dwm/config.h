// -------------------------------- Appearance ---------------------------------

// border pixel of windows
static const unsigned int borderpx  = 1;
// gaps between windows 
static const unsigned int gappx = 6;
// snap pixel 
static const unsigned int snap = 32;
// 0: sloppy systray follows selected monitor, >0: pin systray to monitor X 
static const unsigned int systraypinning = 0;
// systray spacing 
static const unsigned int systrayspacing = 2;
// 1: if pinning fails, display systray on the first monitor, False: display systray on the last monitor
static const int systraypinningfailfirst = 1;
// 0 means no systray
static const int showsystray = 1;
// 0 means no bar 
static const int showbar = 1;
// 0 means bottom bar 
static const int topbar = 1;

// ---------------------------------- Fonts ------------------------------------

static const char *fonts[] = { "UbuntuMono Nerd Font:size=14:weight=bold:antialias=true:autohint:true" };
static const char dmenufont[] = "UbuntuMono Nerd Font:size=12:antialias=true:autohint=true";

// ---------------------------------- Colors -----------------------------------

static const char window_border[] = "#000000";
static const char inactive[] = "#4c566a";
static const char active[] = "#ffffff";

static const char material_bg[] = "#0f101a";
static const char material_focus[] = "#a151d3";

static const char onedark_bg[] = "#1e2127";
static const char onedark_focus[] = "#E06C75";

static const char nord_bg[] = "#2e3440";
static const char nord_focus[] = "#81a1c1";

static const char *colors[][3]      = {
    // fg        bg         border   
    { inactive, material_bg, window_border },
    { active, material_focus,  material_focus  },

    { inactive, onedark_bg, window_border },
    { active, onedark_focus,  onedark_focus  },
    
    { inactive, nord_bg, window_border },
    { active, nord_focus,  nord_focus  },
};

// -------------------------------- Workspaces ---------------------------------

static const char *tags[] = { " ", " ", " ", " ", " ", " ", " ", " ", " " };

static const Rule rules[] = {
    /* xprop(1):
     * WM_CLASS(STRING) = instance, class
     * WM_NAME(STRING) = title
     */

    // class      instance    title       tags mask     isfloating   monitor 
    { "Gimp",     NULL,       NULL,       0,            1,           -1 },
    { "Firefox",  NULL,       NULL,       1 << 8,       0,           -1 },
};

// ---------------------------------- Layouts ----------------------------------

static const float mfact = 0.50;  // factor of master area size [0.05..0.95] 
static const int nmaster = 1;     // number of clients in master area 
static const int resizehints = 1; // 1 means respect size hints in tiled resizals 

#include "layouts.c"
static const Layout layouts[] = {
    // symbol   arrange function
    { "[]",     tile }, // first entry is default 
    { "[F]",    NULL }, // no layout function means floating behavior 
    { "[M]",    monocle },
    { "[C]",    tcl },
    { "[G]",    grid },
    { NULL,     NULL },
};

// -------------------------------- Keybindings --------------------------------

#define MODKEY Mod4Mask

#define TAGKEYS(KEY,TAG) \
    { MODKEY,                       KEY,  view,       {.ui = 1 << TAG} }, \
    { MODKEY|ControlMask,           KEY,  toggleview, {.ui = 1 << TAG} }, \
    { MODKEY|ShiftMask,             KEY,  tag,        {.ui = 1 << TAG} }, \
    { MODKEY|ControlMask|ShiftMask, KEY,  toggletag,  {.ui = 1 << TAG} },

// Helper for spawning shell commands in the pre dwm-5.0 fashion 
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

// Commands
static char dmenumon[2] = "0";
static const char *termcmd[]  = { "alacritty", NULL };
static const char *dmenucmd[] = {
    "dmenu_run", "-m", dmenumon,
    "-fn", dmenufont,
    NULL
};

#include <X11/XF86keysym.h>
static Key keys[] = {

    // ------------------ Windows ------------------

    // Switch between windows
    { MODKEY, XK_j, focusstack, {.i = +1 } },
    { MODKEY, XK_k, focusstack, {.i = -1 } },

    // Change window sizes
    { MODKEY, XK_i, incnmaster, {.i = +1 } },
    { MODKEY|ShiftMask, XK_i, incnmaster, {.i = -1 } },
    { MODKEY|ShiftMask, XK_h, setmfact, {.f = -0.05} },
    { MODKEY|ShiftMask, XK_l, setmfact, {.f = +0.05} },

    // Toggle floating
    { MODKEY|ShiftMask, XK_f, togglefloating, {0} },

    // Toggle bar
    { MODKEY|ShiftMask, XK_b, togglebar, {0} },

    // Move windows in current stack
    { MODKEY|ShiftMask, XK_j, rotatestack, {.i = +1 } },
    { MODKEY|ShiftMask, XK_k, rotatestack, {.i = -1 } },

    // Cycle layouts
    { MODKEY, XK_Tab, cyclelayout, {.i = +1 } },
    { MODKEY|ShiftMask, XK_Tab, cyclelayout,  {.i = -1 } },

    // Increase - decrease gaps
    { MODKEY, XK_g, setgaps, {.i = -1 } },
    { MODKEY|ShiftMask, XK_g, setgaps, {.i = +1 } },

    // Focus next - prev monitor
    { MODKEY, XK_period, focusmon, {.i = +1 } },
    { MODKEY, XK_comma, focusmon, {.i = -1 } },

    // Send window to next - prev monitor
    { MODKEY|ShiftMask, XK_period, tagmon, {.i = +1 } },
    { MODKEY|ShiftMask, XK_comma, tagmon, {.i = -1 } },

    // Change color scheme
    { MODKEY, XK_Left, schemeToggle, {0} },
    { MODKEY, XK_Right, schemeCycle, {0} },

    // Kill window
    { MODKEY, XK_w, killclient, {0} },

    // Restart dwm
    { MODKEY|ControlMask, XK_r, quit, {1} },

    // Quit dwm
    { MODKEY|ControlMask, XK_q, quit, {0} },

    // ---------------- Workspaces -----------------

    TAGKEYS(XK_1, 0)
    TAGKEYS(XK_2, 1)
    TAGKEYS(XK_3, 2)
    TAGKEYS(XK_4, 3)
    TAGKEYS(XK_5, 4)
    TAGKEYS(XK_6, 5)
    TAGKEYS(XK_7, 6)
    TAGKEYS(XK_8, 7)
    TAGKEYS(XK_9, 8)

    // ------------------- Apps --------------------

    // dmenu
    { MODKEY|ShiftMask, XK_Return, spawn, {.v = dmenucmd } },

    // rofi
    { MODKEY, XK_m, spawn, SHCMD("rofi -show drun") },

    // Window nav (rofi)
    { MODKEY|ShiftMask, XK_m, spawn, SHCMD("rofi -show") },

    // Terminal
    { MODKEY, XK_Return, spawn, SHCMD("alacritty") },

    // File explorer
    { MODKEY, XK_e, spawn, SHCMD("pcmanfm") },

    // Browser
    { MODKEY, XK_b, spawn, SHCMD("firefox") },

    // Redshift
    { MODKEY, XK_r, spawn, SHCMD("redshift -O 2400") },
    { MODKEY|ShiftMask, XK_r, spawn, SHCMD("redshift -x") },

    // Screenshot
    { MODKEY, XK_s, spawn, SHCMD("scrot") },

    // ----------------- Hardware ------------------

    // Volume
    {0, XF86XK_AudioLowerVolume, spawn, SHCMD("pactl set-sink-volume @DEFAULT_SINK@ -5%")},
    {0, XF86XK_AudioRaiseVolume, spawn, SHCMD("pactl set-sink-volume @DEFAULT_SINK@ +5%")},
    {0, XF86XK_AudioMute, spawn, SHCMD("pactl set-sink-mute @DEFAULT_SINK@ toggle")},

    // Brightness
    {0, XF86XK_MonBrightnessUp, spawn, SHCMD("brightnessctl set +10%")},
    {0, XF86XK_MonBrightnessDown, spawn, SHCMD("brightnessctl set 10%-")},

};

// click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin 
static Button buttons[] = {
    // click            event mask    button       function         argument 
    { ClkLtSymbol,      0,            Button1,     setlayout,       {0} },
    { ClkLtSymbol,      0,            Button3,     setlayout,       {.v = &layouts[2]} },
    { ClkWinTitle,      0,            Button2,     zoom,            {0} },
    { ClkStatusText,    0,            Button2,     spawn,           {.v = termcmd } },
    { ClkClientWin,     MODKEY,       Button1,     movemouse,       {0} },
    { ClkClientWin,     MODKEY,       Button2,     togglefloating,  {0} },
    { ClkClientWin,     MODKEY,       Button3,     resizemouse,     {0} },
    { ClkTagBar,        0,            Button1,     view,            {0} },
    { ClkTagBar,        0,            Button3,     toggleview,      {0} },
    { ClkTagBar,        MODKEY,       Button1,     tag,             {0} },
    { ClkTagBar,        MODKEY,       Button3,     toggletag,       {0} },
};
