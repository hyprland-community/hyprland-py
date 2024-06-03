class General:
    sensitivity: float = 1.0
    # mouse sensitivity (legacy, may cause bugs if not 1, prefer `input:sensitivity`)
    border_size: int = 1
    # size of the border around windows
    no_border_on_floating: bool = False
    # disable borders for floating windows
    gaps_in: int = 5
    # gaps between windows, also supports css style gaps (top, right, bottom, left -> 5,10,15,20)
    gaps_out: int = 20
    # gaps between windows and monitor edges, also supports css style gaps (top, right, bottom, left -> 5,10,15,20)
    gaps_workspaces: int = 0
    # gaps between workspaces. Stacks with gaps_out.
    col_inactive_border: str = "0xff444444"
    # border color for inactive windows
    col_active_border: str = "0xffffffff"
    # border color for the active window
    col_nogroup_border: str = "0xffffaaff"
    # inactive border color for window that cannot be added to a group (see `denywindowfromgroup` dispatcher)
    col_nogroup_border_active: str = "0xffff00ff"
    # active border color for window that cannot be added to a group
    layout: str = "dwindle"
    # which layout to use. [dwindle/master]
    no_focus_fallback: bool = False
    # if true, will not fall back to the next available window when moving focus in a direction where no window was found
    apply_sens_to_raw: bool = False
    # if on, will also apply the sensitivity to raw mouse output (e.g. sensitivity in games) **NOTICE:** ***really*** not recommended.
    resize_on_border: bool = False
    # enables resizing windows by clicking and dragging on borders and gaps
    extend_border_grab_area: int = 15
    # extends the area around the border where you can click and drag on, only used when `general:resize_on_border` is on.
    hover_icon_on_border: bool = True
    # show a cursor icon when hovering over borders, only used when `general:resize_on_border` is on.
    allow_tearing: bool = False
    # master switch for allowing tearing to occur. See [the Tearing page](../Tearing).
    resize_corner: int = 0
    # force floating windows to use a specific corner when being resized (1-4 going clockwise from top left, 0 to disable)
class Decoration:
    rounding: int = 0
    # rounded corners' radius (in layout px)
    active_opacity: float = 1.0
    # opacity of active windows. [0.0 - 1.0]
    inactive_opacity: float = 1.0
    # opacity of inactive windows. [0.0 - 1.0]
    fullscreen_opacity: float = 1.0
    # opacity of fullscreen windows. [0.0 - 1.0]
    drop_shadow: bool = True
    # enable drop shadows on windows
    shadow_range: int = 4
    # Shadow range ("size") in layout px
    shadow_render_power: int = 3
    # in what power to render the falloff (more power, the faster the falloff) [1 - 4]
    shadow_ignore_window: bool = True
    # if true, the shadow will not be rendered behind the window itself, only around it.
    col_shadow: str = "0xee1a1a1a"
    # shadow's color. Alpha dictates shadow's opacity.
    col_shadow_inactive: str = "unset"
    # inactive shadow color. (if not set, will fall back to col.shadow)
    shadow_offset: tuple = (0.0,0.0)
    # shadow's rendering offset.
    shadow_scale: float = 1.0
    # shadow's scale. [0.0 - 1.0]
    dim_inactive: bool = False
    # enables dimming of inactive windows
    dim_strength: float = 0.5
    # how much inactive windows should be dimmed [0.0 - 1.0]
    dim_special: float = 0.2
    # how much to dim the rest of the screen by when a special workspace is open. [0.0 - 1.0]
    dim_around: float = 0.4
    # how much the `dimaround` window rule should dim by. [0.0 - 1.0]
    screen_shader: str = None
    # a path to a custom shader to be applied at the end of rendering. See `examples/screenShader.frag` for an example.
    name: str = "default"
    # description
    enabled: bool = True
    # enable kawase window background blur
    size: int = 8
    # blur size (distance)
    passes: int = 1
    # the amount of passes to perform
    ignore_opacity: bool = False
    # make the blur layer ignore the opacity of the window
    new_optimizations: bool = True
    # whether to enable further optimizations to the blur. Recommended to leave on, as it will massively improve performance.
    xray: bool = False
    # if enabled, floating windows will ignore tiled windows in their blur. Only available if blur_new_optimizations is true. Will reduce overhead on floating blur significantly.
    noise: float = 0.0117
    # how much noise to apply. [0.0 - 1.0]
    contrast: float = 0.8916
    # contrast modulation for blur. [0.0 - 2.0]
    brightness: float = 0.8172
    # brightness modulation for blur. [0.0 - 2.0]
    vibrancy: float = 0.1696
    # Increase saturation of blurred colors. [0.0 - 1.0]
    vibrancy_darkness: float = 0.0
    # How strong the effect of `vibrancy` is on dark areas . [0.0 - 1.0]
    special: bool = False
    # whether to blur behind the special workspace (note: expensive)
    popups: bool = False
    # whether to blur popups (e.g. right-click menus)
    popups_ignorealpha: float = 0.2
    # works like ignorealpha in layer rules. If pixel opacity is below set value, will not blur. [0.0 - 1.0]
class Animations:
    enabled: bool = True
    # enable animations
    first_launch_animation: bool = True
    # enable first launch animation
class Input:
    kb_model: str = None
    # Appropriate XKB keymap parameter. See the note below.
    kb_layout: str = "us"
    # Appropriate XKB keymap parameter
    kb_variant: str = None
    # Appropriate XKB keymap parameter
    kb_options: str = None
    # Appropriate XKB keymap parameter
    kb_rules: str = None
    # Appropriate XKB keymap parameter
    kb_file: str = None
    # If you prefer, you can use a path to your custom .xkb file.
    numlock_by_default: bool = False
    # Engage numlock by default.
    resolve_binds_by_sym: bool = False
    # Determines how keybinds act when multiple layouts are used. If false, keybinds will always act as if the first specified layout is active. If true, keybinds specified by symbols are activated when you type the respective symbol with the current layout.
    repeat_rate: int = 25
    # The repeat rate for held-down keys, in repeats per second.
    repeat_delay: int = 600
    # Delay before a held-down key is repeated, in milliseconds.
    sensitivity: float = 0.0
    # Sets the mouse input sensitivity. Value is clamped to the range -1.0 to 1.0. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration)
    accel_profile: str = None
    # Sets the cursor acceleration profile. Can be one of `adaptive`, `flat`. Can also be `custom`, see [below](#custom-accel-profiles). Leave empty to use `libinput`'s default mode for your input device. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration) [adaptive/flat/custom]
    force_no_accel: bool = False
    # Force no cursor acceleration. This bypasses most of your pointer settings to get as raw of a signal as possible. **Enabling this is not recommended due to potential cursor desynchronization.**
    left_handed: bool = False
    # Switches RMB and LMB
    scroll_points: str = None
    # Sets the scroll acceleration profile, when `accel_profile` is set to `custom`. Has to be in the form `<step> <points>`. Leave empty to have a flat scroll curve.
    scroll_method: str = None
    # Sets the scroll method. Can be one of `2fg` (2 fingers), `edge`, `on_button_down`, `no_scroll`. [libinput#scrolling](https://wayland.freedesktop.org/libinput/doc/latest/scrolling.html) [2fg/edge/on_button_down/no_scroll]
    scroll_button: int = 0
    # Sets the scroll button. Has to be an int, cannot be a string. Check `wev` if you have any doubts regarding the ID. 0 means default.
    scroll_button_lock: bool = False
    # If the scroll button lock is enabled, the button does not need to be held down. Pressing and releasing the button toggles the button lock, which logically holds the button down or releases it. While the button is logically held down, motion events are converted to scroll events.
    scroll_factor: float = 1.0
    # Multiplier added to scroll movement for external mice. Note that there is a separate setting for [touchpad scroll_factor](#touchpad).
    natural_scroll: bool = False
    # Inverts scrolling direction. When enabled, scrolling moves content directly, rather than manipulating a scrollbar.
    follow_mouse: int = 1
    # Specify if and how cursor movement should affect window focus. See the note below. [0/1/2/3]
    mouse_refocus: bool = True
    # If disabled, mouse focus won't switch to the hovered window unless the mouse crosses a window boundary when `follow_mouse=1`.
    float_switch_override_focus: int = 1
    # If enabled (1 or 2), focus will change to the window under the cursor when changing from tiled-to-floating and vice versa. If 2, focus will also follow mouse on float-to-float switches.
    special_fallthrough: bool = False
    # if enabled, having only floating windows in the special workspace will not block focusing windows in the regular workspace.
    off_window_axis_events: int = 1
    # Handles axis events around (gaps/border for tiled, dragarea/border for floated) a focused window. `0` ignores axis events `1` sends out-of-bound coordinates `2` fakes pointer coordinates to the closest point inside the window `3` warps the cursor to the closest point inside the window
class XkbSettings:
    ...
class FollowMouseCursor:
    ...
class CustomAccelProfiles:
    disable_while_typing: bool = True
    # Disable the touchpad while typing.
    natural_scroll: bool = False
    # Inverts scrolling direction. When enabled, scrolling moves content directly, rather than manipulating a scrollbar.
    scroll_factor: float = 1.0
    # Multiplier applied to the amount of scroll movement.
    middle_button_emulation: bool = False
    # Sending LMB and RMB simultaneously will be interpreted as a middle click. This disables any touchpad area that would normally send a middle click based on location. [libinput#middle-button-emulation](https://wayland.freedesktop.org/libinput/doc/latest/middle-button-emulation.html)
    tap_button_map: str = None
    # Sets the tap button mapping for touchpad button emulation. Can be one of `lrm` (default) or `lmr` (Left, Middle, Right Buttons). [lrm/lmr]
    clickfinger_behavior: bool = False
    # Button presses with 1, 2, or 3 fingers will be mapped to LMB, RMB, and MMB respectively. This disables interpretation of clicks based on location on the touchpad. [libinput#clickfinger-behavior](https://wayland.freedesktop.org/libinput/doc/latest/clickpad-softbuttons.html#clickfinger-behavior)
    tap_to_click: bool = True
    # Tapping on the touchpad with 1, 2, or 3 fingers will send LMB, RMB, and MMB respectively.
    drag_lock: bool = False
    # When enabled, lifting the finger off for a short time while dragging will not drop the dragged item. [libinput#tap-and-drag](https://wayland.freedesktop.org/libinput/doc/latest/tapping.html#tap-and-drag)
    tap_and_drag: bool = False
    # Sets the tap and drag mode for the touchpad
    name: str = "default"
    # description
    transform: int = 0
    # Transform the input from touchdevices. The possible transformations are the same as [those of the monitors](../Monitors/#rotating)
    output: str = "\[\[Auto\]\]"
    # The monitor to bind touch devices. The default is auto-detection. To stop auto-detection, use an empty string or the "\[\[Empty\]\]" value.
    enabled: bool = True
    # Whether input is enabled for touch devices.
    name: str = "default"
    # description
    transform: int = 0
    # transform the input from tablets. The possible transformations are the same as [those of the monitors](../Monitors/#rotating)
    output: str = None
    # the monitor to bind tablets. Empty means unbound.
    region_position: tuple = (0.0,0.0)
    # position of the mapped region in monitor layout.
    region_size: tuple = (0.0,0.0)
    # size of the mapped region. When this variable is set, tablet input will be mapped to the region. [0, 0] or invalid size means unset.
    relative_input: bool = False
    # whether the input should be relative
    left_handed: bool = False
    # if enabled, the tablet will be rotated 180 degrees
    active_area_size: tuple = (0.0,0.0)
    # size of tablet's active area in mm
    active_area_position: tuple = (0.0,0.0)
    # position of the active area in mm
class PerDeviceInputConfig:
    ...
class Gestures:
    workspace_swipe: bool = False
    # enable workspace swipe gesture on touchpad
    workspace_swipe_fingers: int = 3
    # how many fingers for the touchpad gesture
    workspace_swipe_distance: int = 300
    # in px, the distance of the touchpad gesture
    workspace_swipe_touch: bool = False
    # enable workspace swiping from the edge of a touchscreen
    workspace_swipe_invert: bool = True
    # invert the direction
    workspace_swipe_min_speed_to_force: int = 30
    # minimum speed in px per timepoint to force the change ignoring `cancel_ratio`. Setting to `0` will disable this mechanic.
    workspace_swipe_cancel_ratio: float = 0.5
    # how much the swipe has to proceed in order to commence it. (0.7 -> if > 0.7 * distance, switch, if less, revert) [0.0 - 1.0]
    workspace_swipe_create_new: bool = True
    # whether a swipe right on the last workspace should create a new one.
    workspace_swipe_direction_lock: bool = True
    # if enabled, switching direction will be locked when you swipe past the `direction_lock_threshold` (touchpad only).
    workspace_swipe_direction_lock_threshold: int = 10
    # in px, the distance to swipe before direction lock activates (touchpad only).
    workspace_swipe_forever: bool = False
    # if enabled, swiping will not clamp at the neighboring workspaces but continue to the further ones.
    workspace_swipe_use_r: bool = False
    # if enabled, swiping will use the `r` prefix instead of the `m` prefix for finding workspaces.
class Group:
    insert_after_current: bool = True
    # whether new windows in a group spawn after current or at group tail
    focus_removed_window: bool = True
    # whether Hyprland should focus on the window that has just been moved out of the group
    col_border_active: str = "0x66ffff00"
    # active group border color
    col_border_inactive: str = "0x66777700"
    # inactive (out of focus) group border color
    col_border_locked_active: str = "0x66ff5500"
    # active locked group border color
    col_border_locked_inactive: str = "0x66775500"
    # inactive locked group border color
    name: str = "default"
    # description
    enabled: bool = True
    # enables groupbars
    font_family: str = "[[Empty]]"
    # font used to display groupbar titles, use `misc:font_family` if not specified
    font_size: int = 8
    # font size of groupbar title
    gradients: bool = True
    # enables gradients
    height: int = 14
    # height of the groupbar
    stacked: bool = False
    # render the groupbar as a vertical stack
    priority: int = 3
    # sets the decoration priority for groupbars
    render_titles: bool = True
    # whether to render titles in the group bar decoration
    scrolling: bool = True
    # whether scrolling in the groupbar changes group active window
    text_color: str = "0xffffffff"
    # controls the group bar text color
    col_active: str = "0x66ffff00"
    # active group border color
    col_inactive: str = "0x66777700"
    # inactive (out of focus) group border color
    col_locked_active: str = "0x66ff5500"
    # active locked group border color
    col_locked_inactive: str = "0x66775500"
    # inactive locked group border color
class Misc:
    disable_hyprland_logo: bool = False
    # disables the random Hyprland logo / anime girl background. :(
    disable_splash_rendering: bool = False
    # disables the Hyprland splash rendering. (requires a monitor reload to take effect)
    col_splash: str = "0xffffffff"
    # Changes the color of the splash text (requires a monitor reload to take effect).
    font_family: str = "Sans"
    # Set the global default font to render the text including debug fps/notification, config error messages and etc., selected from system fonts.
    splash_font_family: str = "[[Empty]]"
    # Changes the font used to render the splash text, selected from system fonts (requires a monitor reload to take effect).
    force_default_wallpaper: int = -1
    # Enforce any of the 3 default wallpapers. Setting this to `0` or `1` disables the anime background. `-1` means "random". [-1/0/1/2]
    vfr: bool = True
    # controls the VFR status of Hyprland. Heavily recommended to leave enabled to conserve resources.
    vrr: int = 0
    # controls the VRR (Adaptive Sync) of your monitors. 0 - off, 1 - on, 2 - fullscreen only [0/1/2]
    mouse_move_enables_dpms: bool = False
    # If DPMS is set to off, wake up the monitors if the mouse moves.
    key_press_enables_dpms: bool = False
    # If DPMS is set to off, wake up the monitors if a key is pressed.
    always_follow_on_dnd: bool = True
    # Will make mouse focus follow the mouse when drag and dropping. Recommended to leave it enabled, especially for people using focus follows mouse at 0.
    layers_hog_keyboard_focus: bool = True
    # If true, will make keyboard-interactive layers keep their focus on mouse move (e.g. wofi, bemenu)
    animate_manual_resizes: bool = False
    # If true, will animate manual window resizes/moves
    animate_mouse_windowdragging: bool = False
    # If true, will animate windows being dragged by mouse, note that this can cause weird behavior on some curves
    disable_autoreload: bool = False
    # If true, the config will not reload automatically on save, and instead needs to be reloaded with `hyprctl reload`. Might save on battery.
    enable_swallow: bool = False
    # Enable window swallowing
    swallow_regex: str = None
    # The *class* regex to be used for windows that should be swallowed (usually, a terminal). To know more about the list of regex which can be used [use this cheatsheet](https://github.com/ziishaned/learn-regex/blob/master/README.md).
    swallow_exception_regex: str = None
    # The *title* regex to be used for windows that should *not* be swallowed by the windows specified in swallow_regex  (e.g. wev). The regex is matched against the parent (e.g. Kitty) window's title on the assumption that it changes to whatever process it's running.
    focus_on_activate: bool = False
    # Whether Hyprland should focus an app that requests to be focused (an `activate` request)
    no_direct_scanout: bool = True
    # Disables direct scanout. Direct scanout attempts to reduce lag when there is only one fullscreen application on a screen (e.g. game). It is also recommended to set this to true if the fullscreen application shows graphical glitches.
    mouse_move_focuses_monitor: bool = True
    # Whether mouse moving into a different monitor should focus it
    suppress_portal_warnings: bool = False
    # disables warnings about incompatible portal implementations.
    render_ahead_of_time: bool = False
    # [Warning: buggy] starts rendering _before_ your monitor displays a frame in order to lower latency
    render_ahead_safezone: int = 1
    # how many ms of safezone to add to rendering ahead of time. Recommended 1-2.
    allow_session_lock_restore: bool = False
    # if true, will allow you to restart a lockscreen app in case it crashes (red screen of death)
    background_color: str = "0x111111"
    # change the background color. (requires enabled `disable_hyprland_logo`)
    close_special_on_empty: bool = True
    # close the special workspace if the last window is removed
    new_window_takes_over_fullscreen: int = 0
    # if there is a fullscreen window, whether a new tiled window opened should replace the fullscreen one or stay behind. 0 - behind, 1 - takes over, 2 - unfullscreen the current fullscreen window [0/1/2]
    initial_workspace_tracking: int = 1
    # if enabled, windows will open on the workspace they were invoked on. 0 - disabled, 1 - single-shot, 2 - persistent (all children too)
    middle_click_paste: bool = True
    # whether to enable middle-click-paste (aka primary selection)
class Binds:
    pass_mouse_when_bound: bool = False
    # if disabled, will not pass the mouse events to apps / dragging windows around if a keybind has been triggered.
    scroll_event_delay: int = 300
    # in ms, how many ms to wait after a scroll event to allow passing another one for the binds.
    workspace_back_and_forth: bool = False
    # If enabled, an attempt to switch to the currently focused workspace will instead switch to the previous workspace. Akin to i3's _auto_back_and_forth_.
    allow_workspace_cycles: bool = False
    # If enabled, workspaces don't forget their previous workspace, so cycles can be created by switching to the first workspace in a sequence, then endlessly going to the previous workspace.
    workspace_center_on: int = 0
    # Whether switching workspaces should center the cursor on the workspace (0) or on the last active window for that workspace (1)
    focus_preferred_method: int = 0
    # sets the preferred focus finding method when using `focuswindow`/`movewindow`/etc with a direction. 0 - history (recent have priority), 1 - length (longer shared edges have priority)
    ignore_group_lock: bool = False
    # If enabled, dispatchers like `moveintogroup`, `moveoutofgroup` and `movewindoworgroup` will ignore lock per group.
    movefocus_cycles_fullscreen: bool = True
    # If enabled, when on a fullscreen window, `movefocus` will cycle fullscreen, if not, it will move the focus in a direction.
    disable_keybind_grabbing: bool = False
    # If enabled, apps that request keybinds to be disabled (e.g. VMs) will not be able to do so.
    window_direction_monitor_fallback: bool = True
    # If enabled, moving a window or focus over the edge of a monitor with a direction will move it to the next monitor in that direction.
class Xwayland:
    use_nearest_neighbor: bool = True
    # uses the nearest neigbor filtering for xwayland apps, making them pixelated rather than blurry
    force_zero_scaling: bool = False
    # forces a scale of 1 on xwayland windows on scaled displays.
class Opengl:
    nvidia_anti_flicker: bool = True
    # reduces flickering on nvidia at the cost of possible frame drops on lower-end GPUs. On non-nvidia, this is ignored.
    force_introspection: int = 2
    # forces introspection at all times. Introspection is aimed at reducing GPU usage in certain cases, but might cause graphical glitches on nvidia. 0 - nothing, 1 - force always on, 2 - force always on if nvidia
class Cursor:
    no_hardware_cursors: bool = False
    # disables hardware cursors
    hotspot_padding: int = 1
    # the padding, in logical px, between screen edges and the cursor
    inactive_timeout: int = 0
    # in seconds, after how many seconds of cursor's inactivity to hide it. Set to `0` for never.
    no_warps: bool = False
    # if true, will not warp the cursor in many cases (focusing, keybinds, etc)
    default_monitor: str = None
    # the name of a default monitor for the cursor to be set to on startup (see `hyprctl monitors` for names)
    zoom_factor: float = 1.0
    # the factor to zoom by around the cursor. Like a magnifying glass. Minimum 1.0 (meaning no zoom)
    zoom_rigid: bool = False
    # whether the zoom should follow the cursor rigidly (cursor is always centered if it can be) or loosely
    enable_hyprcursor: bool = True
    # whether to enable hyprcursor support
    hide_on_key_press: bool = False
    # Hides the cursor when you press any key until the mouse is moved.
    hide_on_touch: bool = False
    # Hides the cursor when the last input was a touch input until a mouse input is done.
class Debug:
    overlay: bool = False
    # print the debug performance overlay. Disable VFR for accurate results.
    damage_blink: bool = False
    # (epilepsy warning!) flash areas updated with damage tracking
    disable_logs: bool = True
    # disable logging to a file
    disable_time: bool = True
    # disables time logging
    damage_tracking: int = 2
    # redraw only the needed bits of the display. Do **not** change. (default: full - 2) monitor - 1, none - 0
    enable_stdout_logs: bool = False
    # enables logging to stdout
    manual_crash: int = 0
    # set to 1 and then back to 0 to crash Hyprland.
    suppress_errors: bool = False
    # if true, do not display config file parsing errors.
    watchdog_timeout: int = 5
    # sets the timeout in seconds for watchdog to abort processing of a signal of the main thread. Set to 0 to disable.
    disable_scale_checks: bool = False
    # disables verification of the scale factors. Will result in pixel alignment and rounding errors.
    error_limit: int = 5
    # limits the number of displayed config file parsing errors.
    error_position: int = 0
    # sets the position of the error bar. top - 0, bottom - 1
    colored_stdout_logs: bool = True
    # enables colors in the stdout logs.
class More:
    ...
