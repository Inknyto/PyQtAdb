#!/home/nyto/anaconda3/bin//python
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QTextEdit, QDialog, QVBoxLayout, QScrollArea
css_style = """
/* Add your CSS styles here */
QMainWindow {
    background-color: #F5F5F5; /* Set the background color */
}

QPushButton {
    background-color: #007acc; /* Button background color */
    color: white; /* Button text color */
    border: none; /* Remove button borders */
    border-radius:20px;
}

QPushButton:hover {
    background-color: #005eae; /* Button hover color */
    }

/* Add more styles for other widgets as needed */

"""

class I_N_AndroidShell(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Ink Nyto Android Shell")

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget(scroll_area)
        scroll_area.setWidget(self.scroll_content)

        layout = QVBoxLayout(self.scroll_content)

        self.outside_button = QPushButton("Input Text")
        self.outside_button.setFixedSize(300, 100)
        self.outside_button.clicked.connect(self.open_text_dialog)
        layout.addWidget(self.outside_button)

        self.shell_button = QPushButton("$#£||")
        self.shell_button.setFixedSize(300, 100)
        self.shell_button.clicked.connect(self.open_shell_dialog)
        layout.addWidget(self.shell_button)

        grid_layout = QGridLayout()

        buttons = {"key_unknown": "input keyevent 0", "key_soft_left": "input keyevent 1", "key_soft_right": "input keyevent 2", "key_home": "input keyevent 3", "key_back": "input keyevent 4", "key_call": "input keyevent 5", "key_endcall": "input keyevent 6", "key_0": "input keyevent 7", "key_1": "input keyevent 8", "key_2": "input keyevent 9", "key_3": "input keyevent 10", "key_4": "input keyevent 11", "key_5": "input keyevent 12", "key_6": "input keyevent 13", "key_7": "input keyevent 14", "key_8": "input keyevent 15", "key_9": "input keyevent 16", "key_star": "input keyevent 17", "key_pound": "input keyevent 18", "key_dpad_up": "input keyevent 19", "key_dpad_down": "input keyevent 20", "key_dpad_left": "input keyevent 21", "key_dpad_right": "input keyevent 22", "key_dpad_center": "input keyevent 23", "key_volume_up": "input keyevent 24", "key_volume_down": "input keyevent 25", "key_power": "input keyevent 26", "key_camera": "input keyevent 27", "key_clear": "input keyevent 28", "key_a": "input keyevent 29", "key_b": "input keyevent 30", "key_c": "input keyevent 31", "key_d": "input keyevent 32", "key_e": "input keyevent 33", "key_f": "input keyevent 34", "key_g": "input keyevent 35", "key_h": "input keyevent 36", "key_i": "input keyevent 37", "key_j": "input keyevent 38", "key_k": "input keyevent 39", "key_l": "input keyevent 40", "key_m": "input keyevent 41", "key_n": "input keyevent 42", "key_o": "input keyevent 43", "key_p": "input keyevent 44", "key_q": "input keyevent 45", "key_r": "input keyevent 46", "key_s": "input keyevent 47", "key_t": "input keyevent 48", "key_u": "input keyevent 49", "key_v": "input keyevent 50", "key_w": "input keyevent 51", "key_x": "input keyevent 52", "key_y": "input keyevent 53", "key_z": "input keyevent 54", "key_comma": "input keyevent 55", "key_period": "input keyevent 56", "key_alt_left": "input keyevent 57", "key_alt_right": "input keyevent 58", "key_shift_left": "input keyevent 59", "key_shift_right": "input keyevent 60", "key_tab": "input keyevent 61", "key_space": "input keyevent 62", "key_sym": "input keyevent 63", "key_explorer": "input keyevent 64", "key_envelope": "input keyevent 65", "key_enter": "input keyevent 66", "key_del": "input keyevent 67", "key_grave": "input keyevent 68", "key_minus": "input keyevent 69", "key_equals": "input keyevent 70", "key_left_bracket": "input keyevent 71", "key_right_bracket": "input keyevent 72", "key_backslash": "input keyevent 73", "key_semicolon": "input keyevent 74", "key_apostrophe": "input keyevent 75", "key_slash": "input keyevent 76", "key_at": "input keyevent 77", "key_num": "input keyevent 78", "key_headsethook": "input keyevent 79", "key_focus": "input keyevent 80", "key_plus": "input keyevent 81", "key_menu": "input keyevent 82", "key_notification": "input keyevent 83", "key_search": "input keyevent 84", "key_media_play_pause": "input keyevent 85", "key_media_stop": "input keyevent 86", "key_media_next": "input keyevent 87", "key_media_previous": "input keyevent 88", "key_media_rewind": "input keyevent 89", "key_media_fast_forward": "input keyevent 90", "key_mute": "input keyevent 91", "key_page_up": "input keyevent 92", "key_page_down": "input keyevent 93", "key_pictsymbols": "input keyevent 94", "key_switch_charset": "input keyevent 95", "key_button_a": "input keyevent 96", "key_button_b": "input keyevent 97", "key_button_c": "input keyevent 98", "key_button_x": "input keyevent 99", "key_button_y": "input keyevent 100", "key_button_z": "input keyevent 101", "key_button_l1": "input keyevent 102", "key_button_r1": "input keyevent 103", "key_button_l2": "input keyevent 104", "key_button_r2": "input keyevent 105", "key_button_thumbl": "input keyevent 106", "key_button_thumbr": "input keyevent 107", "key_button_start": "input keyevent 108", "key_button_select": "input keyevent 109", "key_button_mode": "input keyevent 110", "key_escape": "input keyevent 111", "key_forward_del": "input keyevent 112", "key_ctrl_left": "input keyevent 113", "key_ctrl_right": "input keyevent 114", "key_caps_lock": "input keyevent 115", "key_scroll_lock": "input keyevent 116", "key_meta_left": "input keyevent 117", "key_meta_right": "input keyevent 118", "key_function": "input keyevent 119", "key_sysrq": "input keyevent 120", "key_break": "input keyevent 121", "key_move_home": "input keyevent 122", "key_move_end": "input keyevent 123", "key_insert": "input keyevent 124", "key_forward": "input keyevent 125", "key_media_play": "input keyevent 126", "key_media_pause": "input keyevent 127", "key_media_close": "input keyevent 128", "key_media_eject": "input keyevent 129", "key_media_record": "input keyevent 130", "key_f1": "input keyevent 131", "key_f2": "input keyevent 132", "key_f3": "input keyevent 133", "key_f4": "input keyevent 134", "key_f5": "input keyevent 135", "key_f6": "input keyevent 136", "key_f7": "input keyevent 137", "key_f8": "input keyevent 138", "key_f9": "input keyevent 139", "key_f10": "input keyevent 140", "key_f11": "input keyevent 141", "key_f12": "input keyevent 142", "key_num_lock": "input keyevent 143", "key_numpad_0": "input keyevent 144", "key_numpad_1": "input keyevent 145", "key_numpad_2": "input keyevent 146", "key_numpad_3": "input keyevent 147", "key_numpad_4": "input keyevent 148", "key_numpad_5": "input keyevent 149", "key_numpad_6": "input keyevent 150", "key_numpad_7": "input keyevent 151", "key_numpad_8": "input keyevent 152", "key_numpad_9": "input keyevent 153", "key_numpad_divide": "input keyevent 154", "key_numpad_multiply": "input keyevent 155", "key_numpad_subtract": "input keyevent 156", "key_numpad_add": "input keyevent 157", "key_numpad_dot": "input keyevent 158", "key_numpad_comma": "input keyevent 159", "key_numpad_enter": "input keyevent 160", "key_numpad_equals": "input keyevent 161", "key_numpad_left_paren": "input keyevent 162", "key_numpad_right_paren": "input keyevent 163", "key_volume_mute": "input keyevent 164", "key_info": "input keyevent 165", "key_channel_up": "input keyevent 166", "key_channel_down": "input keyevent 167", "key_zoom_in": "input keyevent 168", "key_zoom_out": "input keyevent 169", "key_tv": "input keyevent 170", "key_window": "input keyevent 171", "key_guide": "input keyevent 172", "key_dvr": "input keyevent 173", "key_bookmark": "input keyevent 174", "key_captions": "input keyevent 175", "key_settings": "input keyevent 176", "key_tv_power": "input keyevent 177", "key_tv_input": "input keyevent 178", "key_stb_power": "input keyevent 179", "key_stb_input": "input keyevent 180", "key_avr_power": "input keyevent 181", "key_avr_input": "input keyevent 182", "key_prog_red": "input keyevent 183", "key_prog_green": "input keyevent 184", "key_prog_yellow": "input keyevent 185", "key_prog_blue": "input keyevent 186", "key_app_switch": "input keyevent 187", "key_button_1": "input keyevent 188", "key_button_2": "input keyevent 189", "key_button_3": "input keyevent 190", "key_button_4": "input keyevent 191", "key_button_5": "input keyevent 192", "key_button_6": "input keyevent 193", "key_button_7": "input keyevent 194", "key_button_8": "input keyevent 195", "key_button_9": "input keyevent 196", "key_button_10": "input keyevent 197", "key_button_11": "input keyevent 198", "key_button_12": "input keyevent 199", "key_button_13": "input keyevent 200", "key_button_14": "input keyevent 201", "key_button_15": "input keyevent 202", "key_button_16": "input keyevent 203", "key_language_switch": "input keyevent 204", "key_manner_mode": "input keyevent 205", "key_3d_mode": "input keyevent 206", "key_contacts": "input keyevent 207", "key_calendar": "input keyevent 208", "key_music": "input keyevent 209", "key_calculator": "input keyevent 210", "key_zenkaku_hankaku": "input keyevent 211", "key_eisu": "input keyevent 212", "key_muhenkan": "input keyevent 213", "key_henkan": "input keyevent 214", "key_katakana_hiragana": "input keyevent 215", "key_yen": "input keyevent 216", "key_ro": "input keyevent 217", "key_kana": "input keyevent 218", "key_assist": "input keyevent 219", "key_brightness_down": "input keyevent 220", "key_brightness_up": "input keyevent 221", "key_media_audio_track": "input keyevent 222", "key_sleep": "input keyevent 223", "key_wakeup": "input keyevent 224", "key_pairing": "input keyevent 225", "key_media_top_menu": "input keyevent 226", "key_11": "input keyevent 227", "key_12": "input keyevent 228", "key_last_channel": "input keyevent 229", "key_tv_data_service": "input keyevent 230", "key_voice_assist": "input keyevent 231", "key_tv_radio_service": "input keyevent 232", "key_tv_teletext": "input keyevent 233", "key_tv_number_entry": "input keyevent 234", "key_tv_terrestrial_analog": "input keyevent 235", "key_tv_terrestrial_digital": "input keyevent 236", "key_tv_satellite": "input keyevent 237", "key_tv_satellite_bs": "input keyevent 238", "key_tv_satellite_cs": "input keyevent 239", "key_tv_satellite_service": "input keyevent 240", "key_tv_network": "input keyevent 241", "key_tv_antenna_cable": "input keyevent 242", "key_tv_input_hdmi_1": "input keyevent 243", "key_tv_input_hdmi_2": "input keyevent 244", "key_tv_input_hdmi_3": "input keyevent 245", "key_tv_input_hdmi_4": "input keyevent 246", "key_tv_input_composite_1": "input keyevent 247", "key_tv_input_composite_2": "input keyevent 248", "key_tv_input_component_1": "input keyevent 249", "key_tv_input_component_2": "input keyevent 250", "key_tv_input_vga_1": "input keyevent 251", "key_tv_audio_description": "input keyevent 252", "key_tv_audio_description_mix_up": "input keyevent 253", "key_tv_audio_description_mix_down": "input keyevent 254", "key_tv_zoom_mode": "input keyevent 255", "key_tv_contents_menu": "input keyevent 256", "key_tv_media_context_menu": "input keyevent 257", "key_tv_timer_programming": "input keyevent 258", "key_help": "input keyevent 259", "key_navigate_previous": "input keyevent 260", "key_navigate_next": "input keyevent 261", "key_navigate_in": "input keyevent 262", "key_navigate_out": "input keyevent 263", "key_stem_primary": "input keyevent 264", "key_stem_1": "input keyevent 265", "key_stem_2": "input keyevent 266", "key_stem_3": "input keyevent 267", "key_dpad_up_left": "input keyevent 268", "key_dpad_down_left": "input keyevent 269", "key_dpad_up_right": "input keyevent 270", "key_dpad_down_right": "input keyevent 271", "key_media_skip_forward": "input keyevent 272", "key_media_skip_backward": "input keyevent 273", "key_media_step_forward": "input keyevent 274", "key_media_step_backward": "input keyevent 275", "key_soft_sleep": "input keyevent 276", "key_cut": "input keyevent 277", "key_copy": "input keyevent 278", "key_paste": "input keyevent 279", "key_system_navigation_up": "input keyevent 280", "key_system_navigation_down": "input keyevent 281", "key_system_navigation_left": "input keyevent 282", "key_system_navigation_right": "input keyevent 283", "key_all_apps": "input keyevent 284", "key_refresh": "input keyevent 285"}

        row, col = 0, 0
        button_width, button_height = 150, 75

        for key, value in buttons.items():
            button = QPushButton(f"{key} {'('+value.split(' ')[-1]})")
            # button.setStyleSheet("border-radius: 10px;") 
            button.setFixedSize(button_width, button_height)
            button.clicked.connect(lambda _, key=key: self.key_event_clicked(key, buttons))
            grid_layout.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid_layout)

        self.scroll_content.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

    def open_text_dialog(self):
        self.dialog = TextDialog(self)
        self.dialog.exec_()

    def open_shell_dialog(self):
        self.dialog = InputDialog(self)
        self.dialog.exec_()    

    def adb_input_text(self, text):
        os.system("adb shell input text "+text)
        print("Text entered:", text)

    def key_event_clicked(self, key, buttons):
        os.system(f"adb shell {buttons[key]}")
    
    def shell(self, text):
        os.system(text)

class TextDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Text Dialog")
        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit_clicked)

        layout.addWidget(self.text_edit)
        layout.addWidget(submit_button)
        self.setLayout(layout)

    def submit_clicked(self):
        text = self.text_edit.toPlainText()
        if text:
            self.parent().adb_input_text(text)
            self.close()

class InputDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)

        self.setWindowTitle("Input Dialog")
        layout = QVBoxLayout()

        self.textbox = QTextEdit(self)
        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit_clicked)

        layout.addWidget(self.textbox)
        layout.addWidget(submit_button)
        self.setLayout(layout)

    def submit_clicked(self):
        text = self.textbox.toPlainText()
        if text:
            self.parent().shell(text)
            self.close()

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(css_style)
    key_press_app = I_N_AndroidShell()
    key_press_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()