import PySimpleGUI as sg

__FRAME_SIZE__ = (700,250)

__DISPLAY_OPTIONS__ = {
                        "columns": ["1", "2", "3"],
                        "bindToField": ["all", "1", "2"],
                        "scoringBarLocation": ["bottom", "top"],
                        "allianceOrientation": ["standard", "flipped"],
                        "liveScores": ["true", "false"],
                        "mute": ["true", "false"],
                        "muteRandomizationResults": ["true", "false"],
                        "fieldStyleTimer": ["true", "false"],
                        "overlay": ["true", "false"],
                        "overlayColor": {"green": "%2300FF00",
                                         "pink": "%23FF00FF"},
                        "allianceSelectionStyle": ["classic", "hybrid"],
                        "awardsStyle": ["classic", "overlay"],
                        "previewStyle": ["classic", "overlay"],
                        "randomStyle": ["classic", "overlay"],
                        "dualDivisionRankingStyle": "sideBySide",
                        "rankingsFontSize": ["larger", "smaller"],
                        "rankingsShowQR": ["true", "false"],
                        "showMeetRankings": ["true", "false"],
                        "rankingsAllTeams": ["true", "false"]}

__EMPTY_FRAME__ = sg.pin(sg.Frame("Role Settings", 
                           [[sg.Text("Select a Display and New Role to continue.")]],
                           size=__FRAME_SIZE__, key="-EMPTY-FRAME-"))

__AUDIENCE_FRAME__ = sg.pin(sg.Frame("Role Settings",
                        [[sg.Text("Bind to Field:"), sg.Combo(__DISPLAY_OPTIONS__["bindToField"], default_value="all", expand_x=True, readonly=True, key="bindToField-a")],
                         [sg.Checkbox("Use Field-Style Timer:", default=False, key="fieldStyleTimer-a")],
                         [sg.Text("Scoring Bar Location:"), sg.Combo(__DISPLAY_OPTIONS__["scoringBarLocation"], default_value="bottom", expand_x=True, readonly=True, key="scoringBarLocation-a")],
                         [sg.Text("Alliance Orientation:"), sg.Combo(__DISPLAY_OPTIONS__["allianceOrientation"], default_value="standard", expand_x=True, readonly=True, key="allianceOrientation-a")],
                         [sg.Text("Rankings Font Size:"), sg.Combo(__DISPLAY_OPTIONS__["rankingsFontSize"], default_value="larger", expand_x=True, readonly=True, key="rankingsFontSize-a")],
                         [sg.Checkbox("Live Score:", default=True, key="liveScores-a")],
                         [sg.Checkbox("Mute:", default=False, key="mute-a")],
                         [sg.Checkbox("Mute Randomization and Results:", default=False, key="muteRandomizationResults-a")]
                        ],
                        size=__FRAME_SIZE__, key="-AUDIENCE-FRAME-", visible=False))

__FIELD_FRAME__ = sg.pin(sg.Frame("Role Settings",
                        [[sg.Text("Bind to Field:"), sg.Combo(__DISPLAY_OPTIONS__["bindToField"], default_value="all", expand_x=True, readonly=True, key="bindToField-f")],
                         [sg.Checkbox("Use Field-Style Timer:", default=True, key="fieldStyleTimer-f")],
                         [sg.Text("Scoring Bar Location:"), sg.Combo(__DISPLAY_OPTIONS__["scoringBarLocation"], default_value="bottom", expand_x=True, readonly=True, key="scoringBarLocation-f")],
                         [sg.Text("Alliance Orientation:"), sg.Combo(__DISPLAY_OPTIONS__["allianceOrientation"], default_value="standard", expand_x=True, readonly=True, key="allianceOrientation-f")],
                         [sg.Text("Rankings Font Size:"), sg.Combo(__DISPLAY_OPTIONS__["rankingsFontSize"], default_value="larger", expand_x=True, readonly=True, key="rankingsFontSize-f")],
                         [sg.Checkbox("Live Score:", default=True, key="liveScores-f")],
                         [sg.Checkbox("Mute:", default=False, key="mute-f")],
                         [sg.Checkbox("Mute Randomization and Results:", default=False, key="muteRandomizationResults-f")]
                        ],
                        size=__FRAME_SIZE__, key="-FIELD-FRAME-", visible=False))

__INSPECTION_FRAME__ = sg.pin(sg.Frame("Role Settings",
                        [[sg.Text("Number of Columns:"), sg.Combo(__DISPLAY_OPTIONS__["columns"], default_value=2, expand_x=True, readonly=True, key="columns")]
                        ],
                        size=__FRAME_SIZE__, key="-INSPECTION-FRAME-", visible=False))

__PIT_FRAME__ = sg.pin(sg.Frame("Role Settings",
                        [[sg.Text("Rankings Font Size:"), sg.Combo(__DISPLAY_OPTIONS__["rankingsFontSize"], default_value="larger", expand_x=True, readonly=True, key="rankingsFontSize-p")],
                         [sg.Checkbox("Show Online Results QR Code:", default=True, key="rankingsShowQR-p")]
                        ],
                        size=__FRAME_SIZE__, key="-PIT-FRAME-", visible=False))

__SPONSOR_FRAME__ = sg.pin(sg.Frame("Role Settings",
                        [[sg.Text("There are no settings for a sponsor display.")]],
                        size=__FRAME_SIZE__, key="-SPONSOR-FRAME-", visible=False))
