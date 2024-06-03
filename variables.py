from ._util import Section

class General(Section):
    __section_name = "General"
    __section_map = {"sensitivity": {"name": "sensitivity", "description": "mouse sensitivity (legacy, may cause bugs if not 1, prefer `input:sensitivity`)", "type": "float", "default": "1.0"}, "border_size": {"name": "border_size", "description": "size of the border around windows", "type": "int", "default": "1"}, "no_border_on_floating": {"name": "no_border_on_floating", "description": "disable borders for floating windows", "type": "bool", "default": "false"}, "gaps_in": {"name": "gaps_in", "description": "gaps between windows, also supports css style gaps (top, right, bottom, left -> 5,10,15,20)", "type": "int", "default": "5"}, "gaps_out": {"name": "gaps_out", "description": "gaps between windows and monitor edges, also supports css style gaps (top, right, bottom, left -> 5,10,15,20)", "type": "int", "default": "20"}, "gaps_workspaces": {"name": "gaps_workspaces", "description": "gaps between workspaces. Stacks with gaps_out.", "type": "int", "default": "0"}, "col_inactive_border": {"name": "col.inactive_border", "description": "border color for inactive windows", "type": "gradient", "default": "0xff444444"}, "col_active_border": {"name": "col.active_border", "description": "border color for the active window", "type": "gradient", "default": "0xffffffff"}, "col_nogroup_border": {"name": "col.nogroup_border", "description": "inactive border color for window that cannot be added to a group (see `denywindowfromgroup` dispatcher)", "type": "gradient", "default": "0xffffaaff"}, "col_nogroup_border_active": {"name": "col.nogroup_border_active", "description": "active border color for window that cannot be added to a group", "type": "gradient", "default": "0xffff00ff"}, "layout": {"name": "layout", "description": "which layout to use. [dwindle/master]", "type": "str", "default": "dwindle"}, "no_focus_fallback": {"name": "no_focus_fallback", "description": "if true, will not fall back to the next available window when moving focus in a direction where no window was found", "type": "bool", "default": "false"}, "apply_sens_to_raw": {"name": "apply_sens_to_raw", "description": "if on, will also apply the sensitivity to raw mouse output (e.g. sensitivity in games) **NOTICE:** ***really*** not recommended.", "type": "bool", "default": "false"}, "resize_on_border": {"name": "resize_on_border", "description": "enables resizing windows by clicking and dragging on borders and gaps", "type": "bool", "default": "false"}, "extend_border_grab_area": {"name": "extend_border_grab_area", "description": "extends the area around the border where you can click and drag on, only used when `general:resize_on_border` is on.", "type": "int", "default": "15"}, "hover_icon_on_border": {"name": "hover_icon_on_border", "description": "show a cursor icon when hovering over borders, only used when `general:resize_on_border` is on.", "type": "bool", "default": "true"}, "allow_tearing": {"name": "allow_tearing", "description": "master switch for allowing tearing to occur. See [the Tearing page](../Tearing).", "type": "bool", "default": "false"}, "resize_corner": {"name": "resize_corner", "description": "force floating windows to use a specific corner when being resized (1-4 going clockwise from top left, 0 to disable)", "type": "int", "default": "0"}}

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

class Decoration(Section):
    __section_name = "Decoration"
    __section_map = {"rounding": {"name": "rounding", "description": "rounded corners' radius (in layout px)", "type": "int", "default": "0"}, "active_opacity": {"name": "active_opacity", "description": "opacity of active windows. [0.0 - 1.0]", "type": "float", "default": "1.0"}, "inactive_opacity": {"name": "inactive_opacity", "description": "opacity of inactive windows. [0.0 - 1.0]", "type": "float", "default": "1.0"}, "fullscreen_opacity": {"name": "fullscreen_opacity", "description": "opacity of fullscreen windows. [0.0 - 1.0]", "type": "float", "default": "1.0"}, "drop_shadow": {"name": "drop_shadow", "description": "enable drop shadows on windows", "type": "bool", "default": "true"}, "shadow_range": {"name": "shadow_range", "description": "Shadow range (\"size\") in layout px", "type": "int", "default": "4"}, "shadow_render_power": {"name": "shadow_render_power", "description": "in what power to render the falloff (more power, the faster the falloff) [1 - 4]", "type": "int", "default": "3"}, "shadow_ignore_window": {"name": "shadow_ignore_window", "description": "if true, the shadow will not be rendered behind the window itself, only around it.", "type": "bool", "default": "true"}, "col_shadow": {"name": "col.shadow", "description": "shadow's color. Alpha dictates shadow's opacity.", "type": "color", "default": "0xee1a1a1a"}, "col_shadow_inactive": {"name": "col.shadow_inactive", "description": "inactive shadow color. (if not set, will fall back to col.shadow)", "type": "color", "default": "unset"}, "shadow_offset": {"name": "shadow_offset", "description": "shadow's rendering offset.", "type": "vec2", "default": "[0, 0]"}, "shadow_scale": {"name": "shadow_scale", "description": "shadow's scale. [0.0 - 1.0]", "type": "float", "default": "1.0"}, "dim_inactive": {"name": "dim_inactive", "description": "enables dimming of inactive windows", "type": "bool", "default": "false"}, "dim_strength": {"name": "dim_strength", "description": "how much inactive windows should be dimmed [0.0 - 1.0]", "type": "float", "default": "0.5"}, "dim_special": {"name": "dim_special", "description": "how much to dim the rest of the screen by when a special workspace is open. [0.0 - 1.0]", "type": "float", "default": "0.2"}, "dim_around": {"name": "dim_around", "description": "how much the `dimaround` window rule should dim by. [0.0 - 1.0]", "type": "float", "default": "0.4"}, "screen_shader": {"name": "screen_shader", "description": "a path to a custom shader to be applied at the end of rendering. See `examples/screenShader.frag` for an example.", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "name": {"name": "name", "description": "description", "type": "type", "default": "default"}, "enabled": {"name": "enabled", "description": "enable kawase window background blur", "type": "bool", "default": "true"}, "size": {"name": "size", "description": "blur size (distance)", "type": "int", "default": "8"}, "passes": {"name": "passes", "description": "the amount of passes to perform", "type": "int", "default": "1"}, "ignore_opacity": {"name": "ignore_opacity", "description": "make the blur layer ignore the opacity of the window", "type": "bool", "default": "false"}, "new_optimizations": {"name": "new_optimizations", "description": "whether to enable further optimizations to the blur. Recommended to leave on, as it will massively improve performance.", "type": "bool", "default": "true"}, "xray": {"name": "xray", "description": "if enabled, floating windows will ignore tiled windows in their blur. Only available if blur_new_optimizations is true. Will reduce overhead on floating blur significantly.", "type": "bool", "default": "false"}, "noise": {"name": "noise", "description": "how much noise to apply. [0.0 - 1.0]", "type": "float", "default": "0.0117"}, "contrast": {"name": "contrast", "description": "contrast modulation for blur. [0.0 - 2.0]", "type": "float", "default": "0.8916"}, "brightness": {"name": "brightness", "description": "brightness modulation for blur. [0.0 - 2.0]", "type": "float", "default": "0.8172"}, "vibrancy": {"name": "vibrancy", "description": "Increase saturation of blurred colors. [0.0 - 1.0]", "type": "float", "default": "0.1696"}, "vibrancy_darkness": {"name": "vibrancy_darkness", "description": "How strong the effect of `vibrancy` is on dark areas . [0.0 - 1.0]", "type": "float", "default": "0.0"}, "special": {"name": "special", "description": "whether to blur behind the special workspace (note: expensive)", "type": "bool", "default": "false"}, "popups": {"name": "popups", "description": "whether to blur popups (e.g. right-click menus)", "type": "bool", "default": "false"}, "popups_ignorealpha": {"name": "popups_ignorealpha", "description": "works like ignorealpha in layer rules. If pixel opacity is below set value, will not blur. [0.0 - 1.0]", "type": "float", "default": "0.2"}}

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

class Animations(Section):
    __section_name = "Animations"
    __section_map = {"enabled": {"name": "enabled", "description": "enable animations", "type": "bool", "default": "true"}, "first_launch_animation": {"name": "first_launch_animation", "description": "enable first launch animation", "type": "bool", "default": "true"}}

    enabled: bool = True
    # enable animations
    first_launch_animation: bool = True
    # enable first launch animation

class Input(Section):
    __section_name = "Input"
    __section_map = {"kb_model": {"name": "kb_model", "description": "Appropriate XKB keymap parameter. See the note below.", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "kb_layout": {"name": "kb_layout", "description": "Appropriate XKB keymap parameter", "type": "str", "default": "us"}, "kb_variant": {"name": "kb_variant", "description": "Appropriate XKB keymap parameter", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "kb_options": {"name": "kb_options", "description": "Appropriate XKB keymap parameter", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "kb_rules": {"name": "kb_rules", "description": "Appropriate XKB keymap parameter", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "kb_file": {"name": "kb_file", "description": "If you prefer, you can use a path to your custom .xkb file.", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "numlock_by_default": {"name": "numlock_by_default", "description": "Engage numlock by default.", "type": "bool", "default": "false"}, "resolve_binds_by_sym": {"name": "resolve_binds_by_sym", "description": "Determines how keybinds act when multiple layouts are used. If false, keybinds will always act as if the first specified layout is active. If true, keybinds specified by symbols are activated when you type the respective symbol with the current layout.", "type": "bool", "default": "false"}, "repeat_rate": {"name": "repeat_rate", "description": "The repeat rate for held-down keys, in repeats per second.", "type": "int", "default": "25"}, "repeat_delay": {"name": "repeat_delay", "description": "Delay before a held-down key is repeated, in milliseconds.", "type": "int", "default": "600"}, "sensitivity": {"name": "sensitivity", "description": "Sets the mouse input sensitivity. Value is clamped to the range -1.0 to 1.0. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration)", "type": "float", "default": "0.0"}, "accel_profile": {"name": "accel_profile", "description": "Sets the cursor acceleration profile. Can be one of `adaptive`, `flat`. Can also be `custom`, see [below](#custom-accel-profiles). Leave empty to use `libinput`'s default mode for your input device. [libinput#pointer-acceleration](https://wayland.freedesktop.org/libinput/doc/latest/pointer-acceleration.html#pointer-acceleration) [adaptive/flat/custom]", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "force_no_accel": {"name": "force_no_accel", "description": "Force no cursor acceleration. This bypasses most of your pointer settings to get as raw of a signal as possible. **Enabling this is not recommended due to potential cursor desynchronization.**", "type": "bool", "default": "false"}, "left_handed": {"name": "left_handed", "description": "Switches RMB and LMB", "type": "bool", "default": "false"}, "scroll_points": {"name": "scroll_points", "description": "Sets the scroll acceleration profile, when `accel_profile` is set to `custom`. Has to be in the form `<step> <points>`. Leave empty to have a flat scroll curve.", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "scroll_method": {"name": "scroll_method", "description": "Sets the scroll method. Can be one of `2fg` (2 fingers), `edge`, `on_button_down`, `no_scroll`. [libinput#scrolling](https://wayland.freedesktop.org/libinput/doc/latest/scrolling.html) [2fg/edge/on_button_down/no_scroll]", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "scroll_button": {"name": "scroll_button", "description": "Sets the scroll button. Has to be an int, cannot be a string. Check `wev` if you have any doubts regarding the ID. 0 means default.", "type": "int", "default": "0"}, "scroll_button_lock": {"name": "scroll_button_lock", "description": "If the scroll button lock is enabled, the button does not need to be held down. Pressing and releasing the button toggles the button lock, which logically holds the button down or releases it. While the button is logically held down, motion events are converted to scroll events.", "type": "bool", "default": "0"}, "scroll_factor": {"name": "scroll_factor", "description": "Multiplier added to scroll movement for external mice. Note that there is a separate setting for [touchpad scroll_factor](#touchpad).", "type": "float", "default": "1.0"}, "natural_scroll": {"name": "natural_scroll", "description": "Inverts scrolling direction. When enabled, scrolling moves content directly, rather than manipulating a scrollbar.", "type": "bool", "default": "false"}, "follow_mouse": {"name": "follow_mouse", "description": "Specify if and how cursor movement should affect window focus. See the note below. [0/1/2/3]", "type": "int", "default": "1"}, "mouse_refocus": {"name": "mouse_refocus", "description": "If disabled, mouse focus won't switch to the hovered window unless the mouse crosses a window boundary when `follow_mouse=1`.", "type": "bool", "default": "true"}, "float_switch_override_focus": {"name": "float_switch_override_focus", "description": "If enabled (1 or 2), focus will change to the window under the cursor when changing from tiled-to-floating and vice versa. If 2, focus will also follow mouse on float-to-float switches.", "type": "int", "default": "1"}, "special_fallthrough": {"name": "special_fallthrough", "description": "if enabled, having only floating windows in the special workspace will not block focusing windows in the regular workspace.", "type": "bool", "default": "false"}, "off_window_axis_events": {"name": "off_window_axis_events", "description": "Handles axis events around (gaps/border for tiled, dragarea/border for floated) a focused window. `0` ignores axis events `1` sends out-of-bound coordinates `2` fakes pointer coordinates to the closest point inside the window `3` warps the cursor to the closest point inside the window", "type": "int", "default": "1"}}

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

class XkbSettings(Section):
    __section_name = "XKB Settings"
    __section_map = {}


class FollowMouseCursor(Section):
    __section_name = "Follow Mouse Cursor"
    __section_map = {}


class CustomAccelProfiles(Section):
    __section_name = "Custom accel profiles"
    __section_map = {"disable_while_typing": {"name": "disable_while_typing", "description": "Disable the touchpad while typing.", "type": "bool", "default": "true"}, "natural_scroll": {"name": "natural_scroll", "description": "Inverts scrolling direction. When enabled, scrolling moves content directly, rather than manipulating a scrollbar.", "type": "bool", "default": "false"}, "scroll_factor": {"name": "scroll_factor", "description": "Multiplier applied to the amount of scroll movement.", "type": "float", "default": "1.0"}, "middle_button_emulation": {"name": "middle_button_emulation", "description": "Sending LMB and RMB simultaneously will be interpreted as a middle click. This disables any touchpad area that would normally send a middle click based on location. [libinput#middle-button-emulation](https://wayland.freedesktop.org/libinput/doc/latest/middle-button-emulation.html)", "type": "bool", "default": "false"}, "tap_button_map": {"name": "tap_button_map", "description": "Sets the tap button mapping for touchpad button emulation. Can be one of `lrm` (default) or `lmr` (Left, Middle, Right Buttons). [lrm/lmr]", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "clickfinger_behavior": {"name": "clickfinger_behavior", "description": "Button presses with 1, 2, or 3 fingers will be mapped to LMB, RMB, and MMB respectively. This disables interpretation of clicks based on location on the touchpad. [libinput#clickfinger-behavior](https://wayland.freedesktop.org/libinput/doc/latest/clickpad-softbuttons.html#clickfinger-behavior)", "type": "bool", "default": "false"}, "tap_to_click": {"name": "tap-to-click", "description": "Tapping on the touchpad with 1, 2, or 3 fingers will send LMB, RMB, and MMB respectively.", "type": "bool", "default": "true"}, "drag_lock": {"name": "drag_lock", "description": "When enabled, lifting the finger off for a short time while dragging will not drop the dragged item. [libinput#tap-and-drag](https://wayland.freedesktop.org/libinput/doc/latest/tapping.html#tap-and-drag)", "type": "bool", "default": "false"}, "tap_and_drag": {"name": "tap-and-drag", "description": "Sets the tap and drag mode for the touchpad", "type": "bool", "default": "false"}, "name": {"name": "name", "description": "description", "type": "type", "default": "default"}, "transform": {"name": "transform", "description": "transform the input from tablets. The possible transformations are the same as [those of the monitors](../Monitors/#rotating)", "type": "int", "default": "0"}, "output": {"name": "output", "description": "the monitor to bind tablets. Empty means unbound.", "type": "string", "default": "\\[\\[Empty\\]\\]"}, "enabled": {"name": "enabled", "description": "Whether input is enabled for touch devices.", "type": "bool", "default": "true"}, "region_position": {"name": "region_position", "description": "position of the mapped region in monitor layout.", "type": "vec2", "default": "[0, 0]"}, "region_size": {"name": "region_size", "description": "size of the mapped region. When this variable is set, tablet input will be mapped to the region. [0, 0] or invalid size means unset.", "type": "vec2", "default": "[0, 0]"}, "relative_input": {"name": "relative_input", "description": "whether the input should be relative", "type": "bool", "default": "false"}, "left_handed": {"name": "left_handed", "description": "if enabled, the tablet will be rotated 180 degrees", "type": "bool", "default": "false"}, "active_area_size": {"name": "active_area_size", "description": "size of tablet's active area in mm", "type": "vec2", "default": "[0, 0]"}, "active_area_position": {"name": "active_area_position", "description": "position of the active area in mm", "type": "vec2", "default": "[0, 0]"}}

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
    output: str = "auto"
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

class PerDeviceInputConfig(Section):
    __section_name = "Per-device input config"
    __section_map = {}


class Gestures(Section):
    __section_name = "Gestures"
    __section_map = {"workspace_swipe": {"name": "workspace_swipe", "description": "enable workspace swipe gesture on touchpad", "type": "bool", "default": "false"}, "workspace_swipe_fingers": {"name": "workspace_swipe_fingers", "description": "how many fingers for the touchpad gesture", "type": "int", "default": "3"}, "workspace_swipe_distance": {"name": "workspace_swipe_distance", "description": "in px, the distance of the touchpad gesture", "type": "int", "default": "300"}, "workspace_swipe_touch": {"name": "workspace_swipe_touch", "description": "enable workspace swiping from the edge of a touchscreen", "type": "bool", "default": "false"}, "workspace_swipe_invert": {"name": "workspace_swipe_invert", "description": "invert the direction", "type": "bool", "default": "true"}, "workspace_swipe_min_speed_to_force": {"name": "workspace_swipe_min_speed_to_force", "description": "minimum speed in px per timepoint to force the change ignoring `cancel_ratio`. Setting to `0` will disable this mechanic.", "type": "int", "default": "30"}, "workspace_swipe_cancel_ratio": {"name": "workspace_swipe_cancel_ratio", "description": "how much the swipe has to proceed in order to commence it. (0.7 -> if > 0.7 * distance, switch, if less, revert) [0.0 - 1.0]", "type": "float", "default": "0.5"}, "workspace_swipe_create_new": {"name": "workspace_swipe_create_new", "description": "whether a swipe right on the last workspace should create a new one.", "type": "bool", "default": "true"}, "workspace_swipe_direction_lock": {"name": "workspace_swipe_direction_lock", "description": "if enabled, switching direction will be locked when you swipe past the `direction_lock_threshold` (touchpad only).", "type": "bool", "default": "true"}, "workspace_swipe_direction_lock_threshold": {"name": "workspace_swipe_direction_lock_threshold", "description": "in px, the distance to swipe before direction lock activates (touchpad only).", "type": "int", "default": "10"}, "workspace_swipe_forever": {"name": "workspace_swipe_forever", "description": "if enabled, swiping will not clamp at the neighboring workspaces but continue to the further ones.", "type": "bool", "default": "false"}, "workspace_swipe_use_r": {"name": "workspace_swipe_use_r", "description": "if enabled, swiping will use the `r` prefix instead of the `m` prefix for finding workspaces.", "type": "bool", "default": "false"}}

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

class Group(Section):
    __section_name = "Group"
    __section_map = {"insert_after_current": {"name": "insert_after_current", "description": "whether new windows in a group spawn after current or at group tail", "type": "bool", "default": "true"}, "focus_removed_window": {"name": "focus_removed_window", "description": "whether Hyprland should focus on the window that has just been moved out of the group", "type": "bool", "default": "true"}, "col_border_active": {"name": "col.border_active", "description": "active group border color", "type": "gradient", "default": "0x66ffff00"}, "col_border_inactive": {"name": "col.border_inactive", "description": "inactive (out of focus) group border color", "type": "gradient", "default": "0x66777700"}, "col_border_locked_active": {"name": "col.border_locked_active", "description": "active locked group border color", "type": "gradient", "default": "0x66ff5500"}, "col_border_locked_inactive": {"name": "col.border_locked_inactive", "description": "inactive locked group border color", "type": "gradient", "default": "0x66775500"}, "name": {"name": "name", "description": "description", "type": "type", "default": "default"}, "enabled": {"name": "enabled", "description": "enables groupbars", "type": "bool", "default": "true"}, "font_family": {"name": "font_family", "description": "font used to display groupbar titles, use `misc:font_family` if not specified", "type": "string", "default": "[[Empty]]"}, "font_size": {"name": "font_size", "description": "font size of groupbar title", "type": "int", "default": "8"}, "gradients": {"name": "gradients", "description": "enables gradients", "type": "bool", "default": "true"}, "height": {"name": "height", "description": "height of the groupbar", "type": "int", "default": "14"}, "stacked": {"name": "stacked", "description": "render the groupbar as a vertical stack", "type": "bool", "default": "false"}, "priority": {"name": "priority", "description": "sets the decoration priority for groupbars", "type": "int", "default": "3"}, "render_titles": {"name": "render_titles", "description": "whether to render titles in the group bar decoration", "type": "bool", "default": "true"}, "scrolling": {"name": "scrolling", "description": "whether scrolling in the groupbar changes group active window", "type": "bool", "default": "true"}, "text_color": {"name": "text_color", "description": "controls the group bar text color", "type": "color", "default": "0xffffffff"}, "col_active": {"name": "col.active", "description": "active group border color", "type": "gradient", "default": "0x66ffff00"}, "col_inactive": {"name": "col.inactive", "description": "inactive (out of focus) group border color", "type": "gradient", "default": "0x66777700"}, "col_locked_active": {"name": "col.locked_active", "description": "active locked group border color", "type": "gradient", "default": "0x66ff5500"}, "col_locked_inactive": {"name": "col.locked_inactive", "description": "inactive locked group border color", "type": "gradient", "default": "0x66775500"}}

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

class Misc(Section):
    __section_name = "Misc"
    __section_map = {"disable_hyprland_logo": {"name": "disable_hyprland_logo", "description": "disables the random Hyprland logo / anime girl background. :(", "type": "bool", "default": "false"}, "disable_splash_rendering": {"name": "disable_splash_rendering", "description": "disables the Hyprland splash rendering. (requires a monitor reload to take effect)", "type": "bool", "default": "false"}, "col_splash": {"name": "col.splash", "description": "Changes the color of the splash text (requires a monitor reload to take effect).", "type": "color", "default": "0xffffffff"}, "font_family": {"name": "font_family", "description": "Set the global default font to render the text including debug fps/notification, config error messages and etc., selected from system fonts.", "type": "string", "default": "Sans"}, "splash_font_family": {"name": "splash_font_family", "description": "Changes the font used to render the splash text, selected from system fonts (requires a monitor reload to take effect).", "type": "string", "default": "[[Empty]]"}, "force_default_wallpaper": {"name": "force_default_wallpaper", "description": "Enforce any of the 3 default wallpapers. Setting this to `0` or `1` disables the anime background. `-1` means \"random\". [-1/0/1/2]", "type": "int", "default": "-1"}, "vfr": {"name": "vfr", "description": "controls the VFR status of Hyprland. Heavily recommended to leave enabled to conserve resources.", "type": "bool", "default": "true"}, "vrr": {"name": "vrr", "description": "controls the VRR (Adaptive Sync) of your monitors. 0 - off, 1 - on, 2 - fullscreen only [0/1/2]", "type": "int", "default": "0"}, "mouse_move_enables_dpms": {"name": "mouse_move_enables_dpms", "description": "If DPMS is set to off, wake up the monitors if the mouse moves.", "type": "bool", "default": "false"}, "key_press_enables_dpms": {"name": "key_press_enables_dpms", "description": "If DPMS is set to off, wake up the monitors if a key is pressed.", "type": "bool", "default": "false"}, "always_follow_on_dnd": {"name": "always_follow_on_dnd", "description": "Will make mouse focus follow the mouse when drag and dropping. Recommended to leave it enabled, especially for people using focus follows mouse at 0.", "type": "bool", "default": "true"}, "layers_hog_keyboard_focus": {"name": "layers_hog_keyboard_focus", "description": "If true, will make keyboard-interactive layers keep their focus on mouse move (e.g. wofi, bemenu)", "type": "bool", "default": "true"}, "animate_manual_resizes": {"name": "animate_manual_resizes", "description": "If true, will animate manual window resizes/moves", "type": "bool", "default": "false"}, "animate_mouse_windowdragging": {"name": "animate_mouse_windowdragging", "description": "If true, will animate windows being dragged by mouse, note that this can cause weird behavior on some curves", "type": "bool", "default": "false"}, "disable_autoreload": {"name": "disable_autoreload", "description": "If true, the config will not reload automatically on save, and instead needs to be reloaded with `hyprctl reload`. Might save on battery.", "type": "bool", "default": "false"}, "enable_swallow": {"name": "enable_swallow", "description": "Enable window swallowing", "type": "bool", "default": "false"}, "swallow_regex": {"name": "swallow_regex", "description": "The *class* regex to be used for windows that should be swallowed (usually, a terminal). To know more about the list of regex which can be used [use this cheatsheet](https://github.com/ziishaned/learn-regex/blob/master/README.md).", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "swallow_exception_regex": {"name": "swallow_exception_regex", "description": "The *title* regex to be used for windows that should *not* be swallowed by the windows specified in swallow_regex  (e.g. wev). The regex is matched against the parent (e.g. Kitty) window's title on the assumption that it changes to whatever process it's running.", "type": "str", "default": "\\[\\[Empty\\]\\]"}, "focus_on_activate": {"name": "focus_on_activate", "description": "Whether Hyprland should focus an app that requests to be focused (an `activate` request)", "type": "bool", "default": "false"}, "no_direct_scanout": {"name": "no_direct_scanout", "description": "Disables direct scanout. Direct scanout attempts to reduce lag when there is only one fullscreen application on a screen (e.g. game). It is also recommended to set this to true if the fullscreen application shows graphical glitches.", "type": "bool", "default": "true"}, "mouse_move_focuses_monitor": {"name": "mouse_move_focuses_monitor", "description": "Whether mouse moving into a different monitor should focus it", "type": "bool", "default": "true"}, "suppress_portal_warnings": {"name": "suppress_portal_warnings", "description": "disables warnings about incompatible portal implementations.", "type": "bool", "default": "false"}, "render_ahead_of_time": {"name": "render_ahead_of_time", "description": "[Warning: buggy] starts rendering _before_ your monitor displays a frame in order to lower latency", "type": "bool", "default": "false"}, "render_ahead_safezone": {"name": "render_ahead_safezone", "description": "how many ms of safezone to add to rendering ahead of time. Recommended 1-2.", "type": "int", "default": "1"}, "allow_session_lock_restore": {"name": "allow_session_lock_restore", "description": "if true, will allow you to restart a lockscreen app in case it crashes (red screen of death)", "type": "bool", "default": "false"}, "background_color": {"name": "background_color", "description": "change the background color. (requires enabled `disable_hyprland_logo`)", "type": "color", "default": "0x111111"}, "close_special_on_empty": {"name": "close_special_on_empty", "description": "close the special workspace if the last window is removed", "type": "bool", "default": "true"}, "new_window_takes_over_fullscreen": {"name": "new_window_takes_over_fullscreen", "description": "if there is a fullscreen window, whether a new tiled window opened should replace the fullscreen one or stay behind. 0 - behind, 1 - takes over, 2 - unfullscreen the current fullscreen window [0/1/2]", "type": "int", "default": "0"}, "initial_workspace_tracking": {"name": "initial_workspace_tracking", "description": "if enabled, windows will open on the workspace they were invoked on. 0 - disabled, 1 - single-shot, 2 - persistent (all children too)", "type": "int", "default": "1"}, "middle_click_paste": {"name": "middle_click_paste", "description": "whether to enable middle-click-paste (aka primary selection)", "type": "bool", "default": "true"}}

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

class Binds(Section):
    __section_name = "Binds"
    __section_map = {"pass_mouse_when_bound": {"name": "pass_mouse_when_bound", "description": "if disabled, will not pass the mouse events to apps / dragging windows around if a keybind has been triggered.", "type": "bool", "default": "false"}, "scroll_event_delay": {"name": "scroll_event_delay", "description": "in ms, how many ms to wait after a scroll event to allow passing another one for the binds.", "type": "int", "default": "300"}, "workspace_back_and_forth": {"name": "workspace_back_and_forth", "description": "If enabled, an attempt to switch to the currently focused workspace will instead switch to the previous workspace. Akin to i3's _auto_back_and_forth_.", "type": "bool", "default": "false"}, "allow_workspace_cycles": {"name": "allow_workspace_cycles", "description": "If enabled, workspaces don't forget their previous workspace, so cycles can be created by switching to the first workspace in a sequence, then endlessly going to the previous workspace.", "type": "bool", "default": "false"}, "workspace_center_on": {"name": "workspace_center_on", "description": "Whether switching workspaces should center the cursor on the workspace (0) or on the last active window for that workspace (1)", "type": "int", "default": "0"}, "focus_preferred_method": {"name": "focus_preferred_method", "description": "sets the preferred focus finding method when using `focuswindow`/`movewindow`/etc with a direction. 0 - history (recent have priority), 1 - length (longer shared edges have priority)", "type": "int", "default": "0"}, "ignore_group_lock": {"name": "ignore_group_lock", "description": "If enabled, dispatchers like `moveintogroup`, `moveoutofgroup` and `movewindoworgroup` will ignore lock per group.", "type": "bool", "default": "false"}, "movefocus_cycles_fullscreen": {"name": "movefocus_cycles_fullscreen", "description": "If enabled, when on a fullscreen window, `movefocus` will cycle fullscreen, if not, it will move the focus in a direction.", "type": "bool", "default": "true"}, "disable_keybind_grabbing": {"name": "disable_keybind_grabbing", "description": "If enabled, apps that request keybinds to be disabled (e.g. VMs) will not be able to do so.", "type": "bool", "default": "false"}, "window_direction_monitor_fallback": {"name": "window_direction_monitor_fallback", "description": "If enabled, moving a window or focus over the edge of a monitor with a direction will move it to the next monitor in that direction.", "type": "bool", "default": "true"}}

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

class Xwayland(Section):
    __section_name = "XWayland"
    __section_map = {"use_nearest_neighbor": {"name": "use_nearest_neighbor", "description": "uses the nearest neigbor filtering for xwayland apps, making them pixelated rather than blurry", "type": "bool", "default": "true"}, "force_zero_scaling": {"name": "force_zero_scaling", "description": "forces a scale of 1 on xwayland windows on scaled displays.", "type": "bool", "default": "false"}}

    use_nearest_neighbor: bool = True
    # uses the nearest neigbor filtering for xwayland apps, making them pixelated rather than blurry
    force_zero_scaling: bool = False
    # forces a scale of 1 on xwayland windows on scaled displays.

class Opengl(Section):
    __section_name = "OpenGL"
    __section_map = {"nvidia_anti_flicker": {"name": "nvidia_anti_flicker", "description": "reduces flickering on nvidia at the cost of possible frame drops on lower-end GPUs. On non-nvidia, this is ignored.", "type": "bool", "default": "true"}, "force_introspection": {"name": "force_introspection", "description": "forces introspection at all times. Introspection is aimed at reducing GPU usage in certain cases, but might cause graphical glitches on nvidia. 0 - nothing, 1 - force always on, 2 - force always on if nvidia", "type": "int", "default": "2"}}

    nvidia_anti_flicker: bool = True
    # reduces flickering on nvidia at the cost of possible frame drops on lower-end GPUs. On non-nvidia, this is ignored.
    force_introspection: int = 2
    # forces introspection at all times. Introspection is aimed at reducing GPU usage in certain cases, but might cause graphical glitches on nvidia. 0 - nothing, 1 - force always on, 2 - force always on if nvidia

class Cursor(Section):
    __section_name = "Cursor"
    __section_map = {"no_hardware_cursors": {"name": "no_hardware_cursors", "description": "disables hardware cursors", "type": "bool", "default": "false"}, "hotspot_padding": {"name": "hotspot_padding", "description": "the padding, in logical px, between screen edges and the cursor", "type": "int", "default": "1"}, "inactive_timeout": {"name": "inactive_timeout", "description": "in seconds, after how many seconds of cursor's inactivity to hide it. Set to `0` for never.", "type": "int", "default": "0"}, "no_warps": {"name": "no_warps", "description": "if true, will not warp the cursor in many cases (focusing, keybinds, etc)", "type": "bool", "default": "false"}, "default_monitor": {"name": "default_monitor", "description": "the name of a default monitor for the cursor to be set to on startup (see `hyprctl monitors` for names)", "type": "str", "default": "[[EMPTY]]"}, "zoom_factor": {"name": "zoom_factor", "description": "the factor to zoom by around the cursor. Like a magnifying glass. Minimum 1.0 (meaning no zoom)", "type": "float", "default": "1.0"}, "zoom_rigid": {"name": "zoom_rigid", "description": "whether the zoom should follow the cursor rigidly (cursor is always centered if it can be) or loosely", "type": "bool", "default": "false"}, "enable_hyprcursor": {"name": "enable_hyprcursor", "description": "whether to enable hyprcursor support", "type": "bool", "default": "true"}, "hide_on_key_press": {"name": "hide_on_key_press", "description": "Hides the cursor when you press any key until the mouse is moved.", "type": "bool", "default": "false"}, "hide_on_touch": {"name": "hide_on_touch", "description": "Hides the cursor when the last input was a touch input until a mouse input is done.", "type": "bool", "default": "false"}}

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

class Debug(Section):
    __section_name = "Debug"
    __section_map = {"overlay": {"name": "overlay", "description": "print the debug performance overlay. Disable VFR for accurate results.", "type": "bool", "default": "false"}, "damage_blink": {"name": "damage_blink", "description": "(epilepsy warning!) flash areas updated with damage tracking", "type": "bool", "default": "false"}, "disable_logs": {"name": "disable_logs", "description": "disable logging to a file", "type": "bool", "default": "true"}, "disable_time": {"name": "disable_time", "description": "disables time logging", "type": "bool", "default": "true"}, "damage_tracking": {"name": "damage_tracking", "description": "redraw only the needed bits of the display. Do **not** change. (default: full - 2) monitor - 1, none - 0", "type": "int", "default": "2"}, "enable_stdout_logs": {"name": "enable_stdout_logs", "description": "enables logging to stdout", "type": "bool", "default": "false"}, "manual_crash": {"name": "manual_crash", "description": "set to 1 and then back to 0 to crash Hyprland.", "type": "int", "default": "0"}, "suppress_errors": {"name": "suppress_errors", "description": "if true, do not display config file parsing errors.", "type": "bool", "default": "false"}, "watchdog_timeout": {"name": "watchdog_timeout", "description": "sets the timeout in seconds for watchdog to abort processing of a signal of the main thread. Set to 0 to disable.", "type": "int", "default": "5"}, "disable_scale_checks": {"name": "disable_scale_checks", "description": "disables verification of the scale factors. Will result in pixel alignment and rounding errors.", "type": "bool", "default": "false"}, "error_limit": {"name": "error_limit", "description": "limits the number of displayed config file parsing errors.", "type": "int", "default": "5"}, "error_position": {"name": "error_position", "description": "sets the position of the error bar. top - 0, bottom - 1", "type": "int", "default": "0"}, "colored_stdout_logs": {"name": "colored_stdout_logs", "description": "enables colors in the stdout logs.", "type": "bool", "default": "true"}}

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

class More(Section):
    __section_name = "More"
    __section_map = {}


