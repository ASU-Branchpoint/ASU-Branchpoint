#Full definition of all events in the game. Clunky, and only temporarily held in memory.
#TODO: -Multiple copies of events divided by department, assign departments to events.
#      -Fix extremely arbitrary weighting and point assigning for better random insertion.
#TO LIBRARY WRITER: Question difficulty should be capitalized unless secondary shorthand includes capitalized difficulty.
#                   Add a "secondary shorthand" that's longer than existing shorthand to make menus more understandable.
#                       Existing shorthand should remain for the notifications.
#                   defineHelpDesk, defineRD, defineOffice, defineCyber, defineCubicle, defineStorage, defineCopyRoom
#           Thanks!
label defineFull:
    python:

        event_library = [

        {
            "id": "easy_net_001",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A user says websites are not loading, but shared drives and other internal resources still work. What should you check first?",
            "choices": [
                {
                    "answerText": "Test DNS resolution for external domains and compare it to internal name resolution",
                    "score": 6
                },
                {
                    "answerText": "Restart the workstation and retest whether external browsing returns after a clean boot",
                    "score": 4
                },
                {
                    "answerText": "Reinstall the browser and verify whether the pages load correctly afterward",
                    "score": 1
                }
            ],
            "feedback": "If internal resources still work, the strongest first lead is external name resolution rather than general connectivity. Restarting the workstation can help if the issue is tied to a temporary client-side state, but it does not directly test the likely cause. Reinstalling the browser is the weakest choice because the pattern points to resolution or network behavior, not the browser itself.",
            "shorthand": "Network Issue",
            "longhand": "External sites fail, internal resources still work",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_auth_002",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user cannot sign in and gets a wrong password message. What is the best first response?",
            "choices": [
                {
                    "answerText": "Verify keyboard input details such as caps lock, layout, and possible typing mistakes before changing the account",
                    "score": 7
                },
                {
                    "answerText": "Reset the password right away and confirm whether the account accepts the new credential",
                    "score": 5
                },
                {
                    "answerText": "Disable the account temporarily and wait for the user to try again later",
                    "score": 1
                }
            ],
            "feedback": "Simple input problems are common and easy to rule out first. Resetting the password can solve the issue, but it skips a basic check and changes the account state earlier than necessary. Disabling the account is too aggressive for an ordinary sign-in failure.",
            "shorthand": "Account Issue",
            "longhand": "User cannot sign in, wrong password error",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_print_003",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "One user cannot print, but everyone else can. What should you check first?",
            "choices": [
                {
                    "answerText": "Confirm that the correct printer is selected and still available on that specific user's device",
                    "score": 6
                },
                {
                    "answerText": "Restart the shared printer and test whether the user's next print job leaves the queue",
                    "score": 3
                },
                {
                    "answerText": "Replace the print driver on the server and redeploy the printer connection to users",
                    "score": 1
                }
            ],
            "feedback": "Since only one user is affected, the best first check is the local printer selection or device mapping. Restarting the printer may help in some cases, but the limited scope makes a shared hardware issue less convincing. Replacing the server-side driver is broader than needed for a single-user symptom.",
            "shorthand": "Connection Issue",
            "longhand": "Single user cannot print, others can",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_dns_004",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 8,
            "question": "A user can reach a server by IP address but not by hostname. What is the most likely issue?",
            "choices": [
                {
                    "answerText": "The hostname is failing to resolve correctly through DNS or related name services",
                    "score": 8
                },
                {
                    "answerText": "The server is unavailable even though direct network access still appears to work",
                    "score": 2
                }
            ],
            "feedback": "If the server responds by IP, the basic network path is functioning. That makes name resolution the strongest explanation. A server outage does not fit as well because direct access already succeeded.",
            "shorthand": "Network Issue",
            "longhand": "Hostname fails but IP access works",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_perf_005",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user reports their PC is very slow, and Task Manager shows one process using 95% CPU. What should you do first?",
            "choices": [
                {
                    "answerText": "Identify the process and determine whether it is expected, misbehaving, or suspicious before stopping it",
                    "score": 7
                },
                {
                    "answerText": "End the process immediately and watch whether overall responsiveness improves afterward",
                    "score": 5
                },
                {
                    "answerText": "Leave the process alone and continue only if the system becomes completely unusable",
                    "score": 0
                }
            ],
            "feedback": "The best first move is to understand what the process is, since it could be legitimate, broken, or malicious. Ending it may improve performance quickly, but it risks interrupting something important before you know what it does. Ignoring unusually high CPU use leaves the likely cause untouched.",
            "shorthand": "Device Issue",
            "longhand": "High CPU usage causing system slowdown",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_time_006",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A domain user cannot log in, and the workstation clock is several minutes off. What should you do first?",
            "choices": [
                {
                    "answerText": "Synchronize the workstation time with the domain source and retry domain authentication",
                    "score": 6
                },
                {
                    "answerText": "Reset the user's password and test whether a fresh credential resolves the sign-in failure",
                    "score": 3
                },
                {
                    "answerText": "Remove the PC from the domain and join it again to rebuild the machine relationship",
                    "score": 1
                }
            ],
            "feedback": "Time mismatch is a direct problem for domain authentication, especially with Kerberos. Resetting the password changes credentials without addressing the timing issue. Rejoining the domain is much more disruptive than needed for this symptom.",
            "shorthand": "Account Issue",
            "longhand": "Domain login fails due to time mismatch",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_wifi_007",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A laptop user says they cannot connect to Wi-Fi. What is the best first check?",
            "choices": [
                {
                    "answerText": "Confirm that wireless networking is enabled on the device and that airplane mode is not active",
                    "score": 5
                },
                {
                    "answerText": "Replace the wireless router and test whether the user's connection returns afterward",
                    "score": 1
                }
            ],
            "feedback": "Basic client-side state is quick to verify and often resolves the issue immediately. Replacing network hardware is far too large a first step when the problem may be local to the laptop.",
            "shorthand": "Connection Issue",
            "longhand": "Laptop unable to connect to Wi-Fi",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_drive_008",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user cannot access a mapped drive they normally use. What should you check first?",
            "choices": [
                {
                    "answerText": "Verify that the path is reachable and that the user still has the permissions required for that share",
                    "score": 7
                },
                {
                    "answerText": "Restart the file server and test whether the mapped drive reconnects on the next attempt",
                    "score": 3
                },
                {
                    "answerText": "Create a replacement shared folder with the same name so the user has something to reconnect to",
                    "score": 0
                }
            ],
            "feedback": "Mapped drive failures are most often tied to permissions or path reachability. Restarting the server affects everyone and is not well justified as a first check. Creating a new share does not solve the original problem and can make troubleshooting more confusing.",
            "shorthand": "Connection Issue",
            "longhand": "User cannot access mapped network drive",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_mail_009",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A user's emails are stuck in the Outbox. What should you check first?",
            "choices": [
                {
                    "answerText": "Check for a large attachment or a connectivity problem that is preventing the message from leaving",
                    "score": 6
                },
                {
                    "answerText": "Reinstall the email client and confirm whether the queue clears after the reinstall finishes",
                    "score": 2
                },
                {
                    "answerText": "Delete the user's mail profile immediately and rebuild it before doing any other testing",
                    "score": 1
                }
            ],
            "feedback": "Large attachments and connection problems are common reasons mail remains in the Outbox. Reinstalling the client may help in some cases, but it is a heavier step than checking the most likely cause first. Deleting the profile immediately is riskier and skips simple validation.",
            "shorthand": "Software Issue",
            "longhand": "Emails stuck in Outbox, not sending",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_lockout_010",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 8,
            "question": "A user's account keeps locking again shortly after being unlocked. What is the best thing to investigate?",
            "choices": [
                {
                    "answerText": "Look for saved credentials, mobile devices, or background services still trying the old password",
                    "score": 8
                },
                {
                    "answerText": "Continue unlocking the account each time it locks so the user can keep working between lockouts",
                    "score": 4
                },
                {
                    "answerText": "Delete the account and build a replacement user object with the same access permissions",
                    "score": 1
                }
            ],
            "feedback": "Repeated lockouts usually mean something is still using outdated credentials in the background. Repeatedly unlocking the account only treats the symptom. Recreating the account is much more disruptive than needed for a common credential issue.",
            "shorthand": "Account Issue",
            "longhand": "Account repeatedly locking after unlock",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_browser_011",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A website displays incorrectly for one user, but works for others. What is a strong first step?",
            "choices": [
                {
                    "answerText": "Clear the browser cache and reload the site to see whether the incorrect local content is replaced",
                    "score": 5
                },
                {
                    "answerText": "Restart the web server and check whether the single-user display problem disappears afterward",
                    "score": 1
                }
            ],
            "feedback": "Because the issue affects one user, local browser state is a stronger suspect than the website server itself. Restarting the server is not a strong first move for a single-user display problem.",
            "shorthand": "Software Issue",
            "longhand": "Website displays incorrectly for one user",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_disk_012",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A workstation is sluggish and Task Manager shows disk usage near 100%. What should you do first?",
            "choices": [
                {
                    "answerText": "Identify which processes are driving disk activity and compare whether the load looks expected or abnormal",
                    "score": 6
                },
                {
                    "answerText": "Leave the system alone for now and only act if the workstation becomes completely unusable",
                    "score": 0
                }
            ],
            "feedback": "High disk usage usually comes from a specific process or workload, so identifying the source is the strongest first move. Waiting without checking anything leaves the likely cause unresolved.",
            "shorthand": "Device Issue",
            "longhand": "High disk usage causing system slowdown",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_usb_013",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A USB device is not recognized when plugged in. What is the best first step?",
            "choices": [
                {
                    "answerText": "Try another USB port and verify whether the device connection changes at the hardware level",
                    "score": 5
                },
                {
                    "answerText": "Replace the motherboard and test whether the device is detected after the hardware swap",
                    "score": 0
                }
            ],
            "feedback": "Trying another port is fast, low-risk, and directly checks whether the issue is local to the port or connection. Replacing major hardware is not justified as a first troubleshooting step.",
            "shorthand": "Device Issue",
            "longhand": "USB device not recognized by system",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_audio_014",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A user reports no sound from their computer. What should you check first?",
            "choices": [
                {
                    "answerText": "Check the active output device and volume state to confirm audio is routed where the user expects",
                    "score": 5
                },
                {
                    "answerText": "Replace the speakers and test whether new hardware restores the missing sound path",
                    "score": 2
                },
                {
                    "answerText": "Reinstall the operating system and verify whether the rebuilt environment restores audio playback",
                    "score": 0
                }
            ],
            "feedback": "Audio output selection and mute state are common causes of missing sound and are easy to verify first. Replacing speakers may help if hardware is bad, but it is not the strongest first move. Reinstalling the operating system is far too heavy for this symptom.",
            "shorthand": "Device Issue",
            "longhand": "No sound output from user computer",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_update_015",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A system update failed to install. What is the best next step?",
            "choices": [
                {
                    "answerText": "Retry the update and review the error details or logs so the failure can be narrowed down",
                    "score": 6
                },
                {
                    "answerText": "Ignore the update for now and revisit it only if users begin reporting visible issues",
                    "score": 0
                },
                {
                    "answerText": "Wipe the system and rebuild it immediately so the update path starts from a clean image",
                    "score": 1
                }
            ],
            "feedback": "Checking the failure details is the strongest next step because it explains why the update did not apply. Ignoring failed updates can lead to stability or security problems. Rebuilding the system is a last resort, not an initial response.",
            "shorthand": "Software Issue",
            "longhand": "System update failed to install properly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_local_016",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user can sign in with cached credentials while offline, but cannot authenticate to the domain when connected. What should you check first?",
            "choices": [
                {
                    "answerText": "Check whether the workstation can reach and resolve the domain resources needed for authentication",
                    "score": 7
                },
                {
                    "answerText": "Replace the keyboard and confirm whether the new hardware changes the connected sign-in result",
                    "score": 1
                },
                {
                    "answerText": "Create a second account for the user and test whether a new identity reaches the domain correctly",
                    "score": 2
                }
            ],
            "feedback": "Cached credentials explain why offline sign-in works, so the next step is to verify domain connectivity and resolution. Replacing the keyboard does not fit the symptom. Creating another user account avoids the real problem instead of diagnosing domain access.",
            "shorthand": "Connection Issue",
            "longhand": "Offline login works, domain login fails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_memory_017",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A system is slowing down and available memory is almost gone. What is the best first step?",
            "choices": [
                {
                    "answerText": "Check which processes are consuming memory so you can tell whether usage is expected or abnormal",
                    "score": 6
                },
                {
                    "answerText": "Restart the PC immediately and see whether memory usage resets to a stable baseline afterward",
                    "score": 3
                },
                {
                    "answerText": "Replace the monitor so the user can continue working while the slowdown is reassessed later",
                    "score": 0
                }
            ],
            "feedback": "Looking at memory-heavy processes is the best way to tell whether the issue is normal use, a leak, or a runaway app. Restarting may temporarily improve performance but removes useful context before you inspect it. Replacing unrelated hardware does not match the symptom.",
            "shorthand": "Device Issue",
            "longhand": "Low available memory causing system slowdown",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_dhcp_018",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A workstation has no usable IP address. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Check DHCP assignment and verify whether the adapter is receiving or failing to receive a valid lease",
                    "score": 7
                },
                {
                    "answerText": "Replace the workstation and test whether new hardware receives an address normally",
                    "score": 0
                },
                {
                    "answerText": "Map a network drive to see whether the machine can still reach shared resources indirectly",
                    "score": 1
                }
            ],
            "feedback": "A missing or unusable IP address points directly to network configuration or DHCP behavior. Replacing the workstation is too drastic before checking lease assignment. Mapping a drive does not solve or meaningfully diagnose the lack of a valid address.",
            "shorthand": "Network Issue",
            "longhand": "Workstation missing or invalid IP address",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_keyboard_019",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A user says the keyboard is typing the wrong characters. What is the best first check?",
            "choices": [
                {
                    "answerText": "Verify the keyboard language and layout settings to confirm the device is using the expected input map",
                    "score": 5
                },
                {
                    "answerText": "Reinstall the operating system so all keyboard settings return to a default state",
                    "score": 0
                }
            ],
            "feedback": "Unexpected characters are often caused by the wrong layout or language selection. Reinstalling the operating system is much too disruptive for what is commonly a simple settings issue.",
            "shorthand": "Device Issue",
            "longhand": "Keyboard typing incorrect or unexpected characters",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_display_020",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A second monitor is not being detected. What should you do first?",
            "choices": [
                {
                    "answerText": "Check the display cable and monitor settings to confirm the second screen is physically and logically connected",
                    "score": 5
                },
                {
                    "answerText": "Replace the graphics card and see whether the new hardware recognizes both displays correctly",
                    "score": 1
                }
            ],
            "feedback": "Connection and display settings are common reasons a second monitor is missing. Replacing the graphics card is too aggressive as an initial troubleshooting step.",
            "shorthand": "Device Issue",
            "longhand": "Second monitor not detected by system",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_app_021",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "An application will not launch on a user's PC. What is the most useful first step?",
            "choices": [
                {
                    "answerText": "Check for errors, logs, or a hung process so you can tell why the launch is failing",
                    "score": 6
                },
                {
                    "answerText": "Reinstall the full operating system and confirm whether the application launches in the rebuilt environment",
                    "score": 0
                },
                {
                    "answerText": "Delete the application folder immediately and rebuild the app from a fresh install afterward",
                    "score": 1
                }
            ],
            "feedback": "The strongest first move is to gather the information the application is already giving you through errors or process state. Reinstalling the operating system is far too broad. Deleting the application folder immediately is destructive and removes useful context before diagnosis.",
            "shorthand": "Software Issue",
            "longhand": "Application fails to launch on user PC",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_logon_022",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user says logging into Windows takes much longer than usual. What should you check first?",
            "choices": [
                {
                    "answerText": "Check startup items, mapped resources, and any network-dependent actions that run during sign-in",
                    "score": 7
                },
                {
                    "answerText": "Replace the PC so the user can try the same login workflow on fresh hardware",
                    "score": 1
                },
                {
                    "answerText": "Explain that long login times can happen and advise the user to keep waiting each morning",
                    "score": 0
                }
            ],
            "feedback": "Slow logons are often caused by startup apps, scripts, mapped drives, or network waits during sign-in. Replacing the PC is not justified by the symptom alone. Simply telling the user to wait avoids actual troubleshooting.",
            "shorthand": "Account Issue",
            "longhand": "Windows login process unusually slow",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_cache_023",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A user sees old content on a webpage while others see the updated version. What should you try first?",
            "choices": [
                {
                    "answerText": "Clear browser cache or force-refresh the page so the browser requests fresh content from the site",
                    "score": 6
                },
                {
                    "answerText": "Restart the web server and check whether the user's browser begins showing the newer version afterward",
                    "score": 2
                }
            ],
            "feedback": "If only one user sees stale content, local caching is the strongest first explanation. Restarting the web server is more disruptive and less justified for a single-user symptom.",
            "shorthand": "Software Issue",
            "longhand": "User sees outdated webpage content only",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_link_024",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 7},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 5,
            "question": "A desktop cannot connect over Ethernet. What should you check first?",
            "choices": [
                {
                    "answerText": "Check the cable seating and link lights on both the NIC and switch side of the connection",
                    "score": 5
                },
                {
                    "answerText": "Replace the network switch and retest the same workstation on the rebuilt connection path",
                    "score": 1
                }
            ],
            "feedback": "Physical connectivity is the simplest and most relevant first check for an Ethernet failure. Replacing the entire switch is much too broad as an initial response.",
            "shorthand": "Connection Issue",
            "longhand": "Desktop cannot connect via Ethernet",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_access_025",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpDesk,
            "points": 8,
            "question": "A user changed roles recently and now says they are missing access they should have. What should you check first?",
            "choices": [
                {
                    "answerText": "Check the user's current group memberships and compare them to the access expected for the new role",
                    "score": 8
                },
                {
                    "answerText": "Grant the requested access manually so the user can work while the new role settles into place",
                    "score": 4
                },
                {
                    "answerText": "Tell the user to wait a few days before anyone checks the access model or role mapping",
                    "score": 1
                }
            ],
            "feedback": "Role-based access is usually controlled through group membership, so that is the strongest first place to look. Granting manual access may solve the immediate symptom but can bypass the intended permission model. Waiting without checking anything is weak support practice.",
            "shorthand": "Access Issue",
            "longhand": "User missing access after role change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_dns_001",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 20,
            "question": "Users can reach internal servers by IP, but several internal hostnames fail intermittently. What should you check first?",
            "choices": [
                {
                    "answerText": "Review internal DNS records, client DNS settings, and whether stale entries or old cache data are involved",
                    "score": 20
                },
                {
                    "answerText": "Flush DNS on the affected machines and test whether the issue follows specific systems or specific names",
                    "score": 15
                },
                {
                    "answerText": "Restart the impacted servers to refresh services that may not have registered correctly",
                    "score": 7
                }
            ],
            "feedback": "The strongest first step is to verify whether the DNS data itself is wrong, stale, or being queried incorrectly. Flushing client DNS is a reasonable troubleshooting step and may help isolate whether the problem is local caching, but it does not confirm whether the DNS records are actually correct. Restarting servers can sometimes refresh registrations, but it is a broader action that skips verification.",
            "shorthand": "Network Issue",
            "longhand": "Intermittent internal hostname resolution failures",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_gpo_002",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 24,
            "question": "A new Group Policy setting is applying to some users but not others in the same department. What is the best next step?",
            "choices": [
                {
                    "answerText": "Check OU placement, inheritance, and security filtering to confirm the affected users are actually in scope",
                    "score": 24
                },
                {
                    "answerText": "Run gpupdate /force and compare gpresult output between a working user and a failing user",
                    "score": 18
                },
                {
                    "answerText": "Restart the domain controller that processed the most recent policy change to clear any stale state",
                    "score": 8
                }
            ],
            "feedback": "The most reliable answer checks whether the policy is targeted correctly in the first place. Comparing gpresult and forcing updates is a strong troubleshooting step and useful for validation, but it usually comes after or alongside checking scope. Restarting a domain controller is not tightly matched to a scoping issue and is more disruptive.",
            "shorthand": "Access Issue",
            "longhand": "Group Policy applies inconsistently across users",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_vpn_003",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 22,
            "question": "A remote user can connect to VPN, but cannot access internal resources once connected. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Check route assignment, internal DNS resolution, and whether the VPN session received the expected network settings",
                    "score": 22
                },
                {
                    "answerText": "Reinstall the VPN client and verify whether the same issue happens after a clean reconnect",
                    "score": 13
                },
                {
                    "answerText": "Reset the user's password and force a new VPN login session with fresh credentials",
                    "score": 6
                }
            ],
            "feedback": "If VPN connects successfully but internal access fails, the strongest lead is routing, DNS, or tunnel configuration. Reinstalling the client is not unreasonable and may help if the configuration is corrupted, but it is less targeted than checking what settings the tunnel is actually providing. Resetting the password is weak because authentication already worked.",
            "shorthand": "Network Issue",
            "longhand": "VPN connects but no internal resource access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_mail_004",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 21,
            "question": "Several users report Outlook repeatedly asking for credentials, but they can still sign into other services. What should you check first?",
            "choices": [
                {
                    "answerText": "Review cached credentials, authentication prompts, and whether the mail profile is pointing to the expected service endpoint",
                    "score": 21
                },
                {
                    "answerText": "Create a new Outlook profile for one affected user and compare behavior against the current profile",
                    "score": 16
                },
                {
                    "answerText": "Reset passwords for the affected users and monitor whether the prompts stop during the next login cycle",
                    "score": 8
                }
            ],
            "feedback": "Checking cached credentials and endpoint/profile alignment best matches the symptom because other services still authenticate. Building a fresh profile is a solid diagnostic move and may fix the issue, but it is somewhat heavier than first checking credential and endpoint state. Password resets can help in limited cases but are less convincing when the issue is service-specific.",
            "shorthand": "Software Issue",
            "longhand": "Outlook repeatedly prompts for credentials",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_share_005",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 23,
            "question": "A shared folder is accessible to some users but returns access denied for others who should have the same access. What is the best next step?",
            "choices": [
                {
                    "answerText": "Compare share permissions, NTFS permissions, and group membership between a working user and a failing user",
                    "score": 23
                },
                {
                    "answerText": "Grant temporary direct access to an affected user and use that test to narrow down whether the issue is permission-related",
                    "score": 15
                },
                {
                    "answerText": "Restart the file server and verify whether the access denied behavior persists after services reload",
                    "score": 6
                }
            ],
            "feedback": "Comparing a working user and a failing user gives the cleanest path to the underlying permission difference. Granting temporary direct access can help isolate whether permissions are the root cause, but it is more of a workaround and can muddy the access model. Restarting the server is a weaker fit because the problem already looks like authorization, not availability.",
            "shorthand": "Access Issue",
            "longhand": "Shared folder access denied for some users",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_dhcp_006",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 25,
            "question": "Newly connected devices are intermittently failing to receive valid IP addresses. What should you check first?",
            "choices": [
                {
                    "answerText": "Review DHCP scope utilization, lease availability, and whether the DHCP service is handing out addresses correctly",
                    "score": 25
                },
                {
                    "answerText": "Assign temporary static IP addresses to a few affected devices to see whether the issue is limited to lease assignment",
                    "score": 17
                },
                {
                    "answerText": "Restart the affected workstations and test whether new leases are issued after a clean boot",
                    "score": 8
                }
            ],
            "feedback": "Checking DHCP scope health is the best first step because it directly tests whether address assignment is the actual failure. Temporary static IPs can be a useful diagnostic move for isolating DHCP from general connectivity, but they do not explain why leasing is failing. Restarting clients may occasionally help but is less targeted than examining the lease source.",
            "shorthand": "Network Issue",
            "longhand": "Devices intermittently failing to obtain IP",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_web_007",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 18,
            "question": "An internal web application loads fine on Wi-Fi but fails when the same laptop is docked on Ethernet. What should you compare first?",
            "choices": [
                {
                    "answerText": "Compare IP configuration, DNS, gateway, and VLAN behavior between the Wi-Fi and Ethernet connections",
                    "score": 18
                },
                {
                    "answerText": "Swap the docking adapter and verify whether the failure follows the hardware path or the network path",
                    "score": 13
                },
                {
                    "answerText": "Reinstall the application client and test whether the protocol stack re-registers correctly after reinstall",
                    "score": 6
                }
            ],
            "feedback": "Because the same machine behaves differently based on connection type, the strongest first move is to compare the two network paths directly. Swapping the dock or adapter is a fair diagnostic test and can rule out local hardware, but it still comes after checking whether the network settings themselves differ. Reinstalling the application is less tied to the symptom.",
            "shorthand": "Network Issue",
            "longhand": "App works on Wi-Fi, fails Ethernet",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_profile_008",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 19,
            "question": "A user signs into a domain PC and gets a temporary profile instead of their normal desktop. What is the best first step?",
            "choices": [
                {
                    "answerText": "Check event logs, profile path access, and whether the expected profile is loading or failing during sign-in",
                    "score": 19
                },
                {
                    "answerText": "Rename the local profile folder and test whether Windows can build a clean profile path on next login",
                    "score": 14
                },
                {
                    "answerText": "Recreate the entire user account and migrate the user's data into a new identity",
                    "score": 5
                }
            ],
            "feedback": "The best first move is to verify why the profile is failing rather than immediately changing data or identity state. Renaming the profile folder can be a workable fix if corruption is local, but it is more intrusive than checking logs and path access first. Recreating the user account is too broad for a profile loading issue.",
            "shorthand": "Software Issue",
            "longhand": "Temporary profile loaded instead of normal",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_cert_009",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 20,
            "question": "Some users are getting certificate warnings on an internal site, while others are not. What should you check first?",
            "choices": [
                {
                    "answerText": "Compare trust stores, intermediate certificates, and trust-chain behavior between working and failing clients",
                    "score": 20
                },
                {
                    "answerText": "Rebind the current certificate on the web server and test whether client warnings stop after the service refreshes",
                    "score": 14
                },
                {
                    "answerText": "Instruct users to continue through the warning while you confirm whether it is only cosmetic",
                    "score": 2
                }
            ],
            "feedback": "Because only some users are affected, client trust differences and chain validation are the strongest lead. Rebinding the certificate is not unreasonable and may help if the service is presenting the wrong chain, but it is broader than first comparing client trust behavior. Telling users to bypass warnings is unsafe and treats the problem as harmless without verification.",
            "shorthand": "Software Issue",
            "longhand": "Certificate warnings affect only some users",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_script_010",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 22,
            "question": "A login script that maps department drives is not running for several users after a recent OU change. What is the best first step?",
            "choices": [
                {
                    "answerText": "Check GPO links, script path access, and whether the OU move changed inheritance or targeting",
                    "score": 22
                },
                {
                    "answerText": "Run the script manually for one affected user and compare the result with a user who still gets it automatically",
                    "score": 16
                },
                {
                    "answerText": "Recreate the drive mappings as permanent manual mappings for the affected department",
                    "score": 8
                }
            ],
            "feedback": "Since the issue appeared after an OU move, policy scope and inheritance are the strongest first checks. Running the script manually is a useful validation step and can separate script failure from policy delivery failure, but it does not answer why the targeting changed. Manual permanent mappings restore function but sidestep the root cause.",
            "shorthand": "Access Issue",
            "longhand": "Login script fails after OU change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_trust_011",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 28,
            "question": "A workstation suddenly shows a trust relationship error when a domain user tries to sign in. What is the best next step?",
            "choices": [
                {
                    "answerText": "Repair the workstation trust with the domain or rejoin the machine after confirming the trust issue/",
                    "score": 28
                },
                {
                    "answerText": "Test domain reachability and secure channel behavior from the workstation before changing the machine account state",
                    "score": 21
                },
                {
                    "answerText": "Reset the user's password and retry sign-in using a fresh credential token",
                    "score": 7
                }
            ],
            "feedback": "Repairing the machine trust is the best corrective step when the trust relationship is actually broken. Testing secure channel behavior and connectivity first is also a strong answer because it confirms the diagnosis before making changes, but it is slightly less direct as an immediate next step. Resetting the user's password does not fit a machine trust failure.",
            "shorthand": "Network Issue",
            "longhand": "Workstation trust relationship with domain broken",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_service_012",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 24,
            "question": "A Windows service starts successfully, then stops after a few seconds. What should you check first?",
            "choices": [
                {
                    "answerText": "Check dependency services, startup parameters, and event log entries tied to the service shutdown",
                    "score": 24
                },
                {
                    "answerText": "Change the service account and retry the startup to test whether the failure is tied to credentials",
                    "score": 16
                },
                {
                    "answerText": "Restart the server so the service has a clean startup environment and test whether it holds",
                    "score": 9
                }
            ],
            "feedback": "Looking at dependencies and logs is the strongest first move because the service is starting and then immediately failing for a reason that should be visible. Changing the service account can be a good targeted diagnostic if identity is suspected, but it is still a change before diagnosis. Restarting the server may help in edge cases but is broader and less informative.",
            "shorthand": "Software Issue",
            "longhand": "Service starts then stops unexpectedly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_spooler_013",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 23,
            "question": "A printer deployed by policy appears on user machines, but jobs remain stuck in queue and never print. What should you check first?",
            "choices": [
                {
                    "answerText": "Check spooler health, printer queue status, and driver compatibility on the print path",
                    "score": 23
                },
                {
                    "answerText": "Remove and redeploy the printer to one affected machine to test whether the deployment artifact is corrupted",
                    "score": 15
                },
                {
                    "answerText": "Change the printer to a generic driver immediately and see whether jobs begin moving afterward",
                    "score": 11
                }
            ],
            "feedback": "The strongest answer checks the actual queue, spooler, and driver interaction first because the printer is already present but failing to process jobs. Redeploying to one machine is a fair test and may isolate whether the deployment object is bad, but it is not as direct as checking the queue path. Swapping to a generic driver might work, yet it changes configuration before confirming the real cause.",
            "shorthand": "Connection Issue",
            "longhand": "Print jobs stuck despite printer deployment",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_delays_014",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 26,
            "question": "Email delivery is delayed for many users across the organization, but messages eventually arrive. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Review the transport queue, delivery retry behavior, and any service or connector health alerts",
                    "score": 26
                },
                {
                    "answerText": "Send controlled test messages between internal and external recipients to narrow down where the delay appears",
                    "score": 19
                },
                {
                    "answerText": "Restart mail clients on affected user machines and compare whether new messages leave the Outbox faster",
                    "score": 6
                }
            ],
            "feedback": "Checking transport and queue health is the strongest first step because the symptom is organization-wide and server-side behavior is most likely. Running controlled message tests is also a good diagnostic approach and helps isolate where delay occurs, but it comes slightly after checking the queueing system directly. Restarting clients is weak for a broad delivery delay.",
            "shorthand": "Software Issue",
            "longhand": "Organization-wide email delivery delays occurring",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_perf_015",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 21,
            "question": "An internal application became slow for everyone immediately after a version update. What is the best first step?",
            "choices": [
                {
                    "answerText": "Review the change introduced by the update and compare current logs or configuration with the pre-update state",
                    "score": 21
                },
                {
                    "answerText": "Roll one server back to the previous version in a controlled test and compare performance behavior",
                    "score": 17
                },
                {
                    "answerText": "Increase server resources and monitor whether the slowdown is reduced under the new version",
                    "score": 10
                }
            ],
            "feedback": "Checking the update and comparing logs/config is the strongest starting point because the timing directly implicates the change. A controlled rollback test is also a strong option and can validate whether the update caused the slowdown, but it is a more active change. Increasing resources may help performance, yet it assumes capacity is the problem rather than the update itself.",
            "shorthand": "Network Issue",
            "longhand": "Application slow after recent version update",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_ports_016",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 22,
            "question": "A service shows as running on the server, but clients cannot connect to it. What should you check first?",
            "choices": [
                {
                    "answerText": "Verify the expected listening ports, network reachability, and any firewall rules between clients and the service",
                    "score": 22
                },
                {
                    "answerText": "Restart the service and confirm whether it binds to the correct interface after a clean start",
                    "score": 15
                },
                {
                    "answerText": "Reinstall the client on one affected machine to see whether the problem is application-side only",
                    "score": 7
                }
            ],
            "feedback": "If a service is running but unreachable, the strongest lead is whether it is truly listening and reachable across the network path. Restarting the service is a fair secondary step and may help if binding failed, but it is less informative than checking the port state directly. Reinstalling a client is weaker because the symptom may exist before the client even reaches the service.",
            "shorthand": "Device Issue",
            "longhand": "Service running but clients cannot connect",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_dns_017",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 27,
            "question": "Internal users are being sent to the wrong internal site when using a hostname that should point elsewhere. What should you check first?",
            "choices": [
                {
                    "answerText": "Check internal DNS data, stale records, and cached resolution on both clients and relevant servers",
                    "score": 27
                },
                {
                    "answerText": "Test the hostname from multiple subnets and compare whether the incorrect destination appears consistently or only in certain places",
                    "score": 21
                },
                {
                    "answerText": "Restart the site that should be receiving traffic so it can re-register itself in the environment",
                    "score": 9
                }
            ],
            "feedback": "Checking the actual DNS data and cache state is the strongest first move because the hostname is resolving to the wrong destination. Testing from multiple subnets is also a strong diagnostic action and helps isolate scope, but it usually follows or complements direct DNS inspection. Restarting the application site is weaker because the symptom is name resolution, not availability alone.",
            "shorthand": "Access Issue",
            "longhand": "Hostname resolving to incorrect internal destination",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_disk_018",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 24,
            "question": "A file server suddenly reports critically low disk space overnight. What is the best first step?",
            "choices": [
                {
                    "answerText": "Review recent growth, large file creation, logs, and scheduled jobs before deleting or expanding anything",
                    "score": 24
                },
                {
                    "answerText": "Expand the volume temporarily and use the added space to gather data without immediate user impact",
                    "score": 17
                },
                {
                    "answerText": "Delete the newest large files to restore service quickly and investigate later",
                    "score": 8
                }
            ],
            "feedback": "The strongest answer investigates why space disappeared before changing or removing data. Expanding the volume can be a reasonable stabilization step if the situation is critical, but it still avoids the cause and may delay root-cause analysis. Deleting files immediately can destroy useful data or evidence and is riskier.",
            "shorthand": "Network Issue",
            "longhand": "File server disk space suddenly depleted",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_ad_019",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 26,
            "question": "A user's group membership was changed on one domain controller, but another system still does not reflect the change hours later. What should you check first?",
            "choices": [
                {
                    "answerText": "Check replication status and whether the relevant domain controllers are exchanging changes normally",
                    "score": 26
                },
                {
                    "answerText": "Sign the user out and back in to force a fresh token and test whether the issue is token-related rather than replication-related",
                    "score": 17
                },
                {
                    "answerText": "Recreate the user account and reapply the desired group memberships from scratch",
                    "score": 5
                }
            ],
            "feedback": "If one domain controller has the change and another appears not to, replication is the strongest first thing to examine. Refreshing the user's token is a reasonable diagnostic move if the directory change has already replicated and the symptom is authorization, but the prompt suggests the directory state itself is inconsistent. Recreating the user is excessive.",
            "shorthand": "Access Issue",
            "longhand": "AD changes not replicating across controllers",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_vlan_020",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 23,
            "question": "A user moved desks and can reach the internet, but cannot access internal systems they used before. What is the best first check?",
            "choices": [
                {
                    "answerText": "Check whether the new switch port and subnet placement put the device on the expected VLAN and internal route path",
                    "score": 23
                },
                {
                    "answerText": "Compare the moved user's IP details to a nearby workstation that still has normal internal access",
                    "score": 18
                },
                {
                    "answerText": "Reinstall the user's machine on the assumption that the move corrupted the network profile",
                    "score": 4
                }
            ],
            "feedback": "Because the issue began after a desk move, checking VLAN or switch-port placement is the strongest answer. Comparing the moved workstation's network details to a working one is also a very good diagnostic step and closely related, but it is slightly less direct than checking the port configuration itself. Reinstalling the machine is poorly matched to the timing.",
            "shorthand": "Network Issue",
            "longhand": "User moved desks, lost internal access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_roaming_021",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 20,
            "question": "A user's desktop settings and documents are not following them between domain PCs as expected. What should you check first?",
            "choices": [
                {
                    "answerText": "Check whether roaming profile or folder redirection settings are applying and whether the profile path is reachable",
                    "score": 20
                },
                {
                    "answerText": "Compare one working user and one failing user to confirm whether the issue is tied to policy application or path access",
                    "score": 16
                },
                {
                    "answerText": "Copy the user's data manually between systems until the normal profile behavior resumes",
                    "score": 8
                }
            ],
            "feedback": "Checking the profile or folder redirection configuration is the best first move because it addresses the mechanism intended to carry settings and documents. Comparing a working user to a failing user is also a strong diagnostic approach, but it usually supports the same underlying check rather than replacing it. Manual copying is only a workaround.",
            "shorthand": "Network Issue",
            "longhand": "User profile data not roaming correctly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_proxy_022",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 22,
            "question": "Several users can browse some websites but fail on others after a recent network configuration change. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Review proxy settings, filtering rules, and the exact change that altered outbound web handling",
                    "score": 22
                },
                {
                    "answerText": "Run controlled tests from more than one client to compare which destinations fail and whether the issue follows user, site, or path",
                    "score": 17
                },
                {
                    "answerText": "Reinstall the browsers used by the affected users to eliminate client-side corruption as a factor",
                    "score": 6
                }
            ],
            "feedback": "The strongest answer focuses on the recent network change and the policy layer that now treats destinations differently. Controlled client tests are also useful and can help isolate scope, but they come just after examining the configuration change itself. Reinstalling browsers is less convincing when multiple users are affected after a network change.",
            "shorthand": "Software Issue",
            "longhand": "Some websites fail after network change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_backup_023",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 9},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 25,
            "question": "Backups have been completing successfully for weeks, but restore tests are failing. What is the best next step?",
            "choices": [
                {
                    "answerText": "Review backup job logs, restore settings, and whether the backups are complete and usable rather than only marked successful",
                    "score": 25
                },
                {
                    "answerText": "Run a limited restore to a test location using the most recent successful set and compare the failure details against earlier sets",
                    "score": 19
                },
                {
                    "answerText": "Run the backups again on the next cycle before looking deeper into restore behavior",
                    "score": 8
                }
            ],
            "feedback": "The best answer checks whether the backup chain and restore configuration are actually valid. Running a controlled restore test is also a strong option and helps narrow the failure, but it is slightly more active than first reading the job and restore details already available. Re-running backups without diagnosing restore failure avoids the core issue.",
            "shorthand": "Software Issue",
            "longhand": "Backups succeed but restores fail",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sched_024",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 8},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineHelpDesk,
            "points": 21,
            "question": "A task that should run nightly on a server has stopped running, but the script still works when launched manually. What should you check first?",
            "choices": [
                {
                    "answerText": "Check Task Scheduler triggers, execution history, and the credentials or permissions used by the scheduled context",
                    "score": 21
                },
                {
                    "answerText": "Create a duplicate scheduled task under a different account and compare whether it executes successfully overnight",
                    "score": 16
                },
                {
                    "answerText": "Run the task manually each morning until the schedule starts working again",
                    "score": 7
                }
            ],
            "feedback": "Because the script works manually, the scheduler context is the strongest first area to inspect. Creating a duplicate task under another account is a valid diagnostic test, but it is a change rather than an initial inspection. Running the task manually is only a workaround and does not explain why the schedule broke.",
            "shorthand": "Software Issue",
            "longhand": "Scheduled task not running automatically",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_auth_025",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 6}
            },
            "location": defineHelpDesk,
            "points": 27,
            "question": "Users can authenticate to some internal services but fail on others after a recent DNS change. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Check whether the affected services now resolve to the correct systems and whether service-related DNS records still match expectations",
                    "score": 27
                },
                {
                    "answerText": "Compare a working service and a failing service from the same client to see whether the failure follows hostname, endpoint, or service type",
                    "score": 21
                },
                {
                    "answerText": "Reset passwords for the affected users and clear all saved credentials before testing again",
                    "score": 7
                }
            ],
            "feedback": "Because the failures began after a DNS change and only affect some services, checking how those services resolve is the strongest answer. Comparing a working and failing service from the same client is also a strong troubleshooting move and can help isolate whether the issue is resolution or service-specific, but it still follows the same underlying hypothesis. Password resets are a weaker fit.",
            "shorthand": "Account Issue",
            "longhand": "Authentication failures after DNS configuration change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_auth_001",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 42,
            "question": "Several users intermittently fail domain authentication. Logs show Kerberos errors, but password resets do not help. What should you check first?",
            "choices": [
                {
                    "answerText": "Review time synchronization and DNS pathing for affected clients and domain controllers involved in the failures",
                    "score": 42
                },
                {
                    "answerText": "Capture one failed sign-in path and compare it to a successful sign-in path to identify whether the issue follows a specific DC or client group",
                    "score": 34
                },
                {
                    "answerText": "Restart the affected clients and domain controllers in a controlled order to clear stale authentication state",
                    "score": 16
                },
                {
                    "answerText": "Reset the passwords again and require all affected users to sign in with fresh credentials",
                    "score": 7
                }
            ],
            "feedback": "Checking time sync and DNS is the strongest first move because Kerberos depends directly on both. Comparing failed and successful sign-ins is also a very strong diagnostic step and helps narrow scope, but it is slightly less direct than first validating the core Kerberos dependencies already suggested by the logs. Restarting systems may help with stale state but does not explain the cause. Additional password resets are weak because that angle has already been tested.",
            "shorthand": "Account Issue",
            "longhand": "Intermittent Kerberos authentication failures across users",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_002",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 45,
            "question": "Multiple users report intermittent connectivity loss. Network logs show repeated ARP conflicts. What is the best first response?",
            "choices": [
                {
                    "answerText": "Trace the conflicting ARP entries to identify the duplicate IP assignment and correct the addressing issue/",
                    "score": 45
                },
                {
                    "answerText": "Isolate one impacted segment and compare switch tables or client lease data to determine whether the conflict is DHCP-driven or static",
                    "score": 36
                },
                {
                    "answerText": "Restart the affected switches to clear learned state and see whether the conflict pattern resets",
                    "score": 15
                },
                {
                    "answerText": "Assign new static IPs to the impacted users so they can reconnect while the rest of the network settles",
                    "score": 11
                }
            ],
            "feedback": "The strongest answer directly identifies the duplicate addressing source causing the ARP conflict. Segment-level isolation and comparison of leases versus static assignments is also very strong and useful for narrowing the cause, but it is slightly less direct than resolving the conflicting entries themselves. Restarting switches may hide the issue temporarily without fixing it. Assigning more static IPs can make address management worse.",
            "shorthand": "Network Issue",
            "longhand": "Network instability caused by ARP IP conflicts",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_ad_003",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 44,
            "question": "Changes made on one domain controller are not appearing on another site hours later. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Review replication health, site-link behavior, and the connectivity path between the affected domain controllers",
                    "score": 44
                },
                {
                    "answerText": "Compare directory metadata on both controllers to confirm whether the delay is replication, lingering objects, or stale reads",
                    "score": 35
                },
                {
                    "answerText": "Restart both domain controllers so replication services reinitialize and retry the pending changes",
                    "score": 16
                },
                {
                    "answerText": "Recreate the missing changes manually on the second site to restore consistency more quickly",
                    "score": 12
                }
            ],
            "feedback": "Checking replication health and inter-site behavior is the strongest first move because the problem is cross-site inconsistency. Comparing metadata is also a strong investigative option and can help distinguish several replication failure modes, but it follows the same diagnosis path rather than replacing the initial health check. Restarting controllers is broader and less precise. Manual recreation risks masking the actual replication issue.",
            "shorthand": "Access Issue",
            "longhand": "Domain controller replication delay across sites",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_dns_004",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 41,
            "question": "Internal users are intermittently sent to the wrong internal server by hostname. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the DNS records, cache state, and stale registration behavior tied to the hostname in question",
                    "score": 41
                },
                {
                    "answerText": "Query the hostname from multiple client groups and compare whether the wrong destination follows subnet, resolver, or client cache",
                    "score": 33
                },
                {
                    "answerText": "Restart the intended application server and force it to reregister its network identity",
                    "score": 13
                },
                {
                    "answerText": "Hardcode the expected IP on the affected clients until normal resolution behavior returns",
                    "score": 10
                }
            ],
            "feedback": "Checking the DNS data and cache state is the strongest first step because the hostname is resolving incorrectly. Multi-client testing is also a strong diagnostic method and helps isolate scope, but it is slightly less direct than checking the resolution source itself. Restarting the target server may help if registration failed, but it is still a broader action. Hardcoding clients is a workaround that creates future maintenance problems.",
            "shorthand": "Network Issue",
            "longhand": "Hostname resolves to incorrect internal servers",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_security_005",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 50,
            "question": "Multiple user accounts show failed sign-in attempts from unfamiliar external IP addresses within a short time window. What is the best first action?",
            "choices": [
                {
                    "answerText": "Contain the affected accounts and escalate as a likely security incident while preserving the relevant authentication evidence",
                    "score": 50
                },
                {
                    "answerText": "Correlate the failed sign-ins across accounts and services first so you can confirm whether the pattern is password spray before containment",
                    "score": 38
                },
                {
                    "answerText": "Reset the affected passwords immediately and continue monitoring whether the attempts persist afterward",
                    "score": 24
                },
                {
                    "answerText": "Wait to see whether the activity escalates into successful logins before involving security responders",
                    "score": 5
                }
            ],
            "feedback": "Containment and escalation are strongest because the pattern already suggests an active threat. Correlation work is useful and can sharpen the incident picture, but it should not delay a reasonable containment response. Password resets may help reduce immediate exposure but do not address the broader event on their own. Waiting for successful compromise is too passive.",
            "shorthand": "Network Issue",
            "longhand": "Multiple failed logins from suspicious external sources",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_backup_006",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 43,
            "question": "Backup jobs have been reporting success, but test restores consistently fail. What should you do first?",
            "choices": [
                {
                    "answerText": "Review backup logs, restore settings, and chain integrity to determine why valid backups are not producing valid restores",
                    "score": 43
                },
                {
                    "answerText": "Perform a controlled restore from more than one backup point to determine whether the failure is tied to a specific generation or the restore workflow itself",
                    "score": 35
                },
                {
                    "answerText": "Run another backup cycle before testing restores again so the newest set is definitely fresh",
                    "score": 11
                },
                {
                    "answerText": "Delete the existing backup set and rebuild the schedule from scratch to eliminate any legacy issues",
                    "score": 8
                }
            ],
            "feedback": "The strongest answer examines why restore functionality is broken even though backups show success. Controlled restores across more than one generation are also a strong diagnostic move and help isolate whether the problem is data-set specific or workflow-specific, but they follow closely after checking the restore and backup details already available. Re-running backups does not fix restore failure. Deleting backups too early risks losing usable recovery points.",
            "shorthand": "Software Issue",
            "longhand": "Backup success reported but restore consistently failing",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_vpn_007",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 46,
            "question": "VPN users are receiving IPs from an unexpected network range and cannot reach protected internal systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the VPN address pool, route assignment, and any access rules tied to the issued range",
                    "score": 46
                },
                {
                    "answerText": "Capture a working and failing VPN session to compare assigned routes, DNS, and policy attributes side by side",
                    "score": 37
                },
                {
                    "answerText": "Restart the VPN service and compare whether the next sessions return to the expected address pool",
                    "score": 15
                },
                {
                    "answerText": "Assign manual static addresses to the remote users who need immediate access",
                    "score": 8
                }
            ],
            "feedback": "Checking the VPN pool and policy logic is the best first move because the wrong addresses are being assigned at the source. Comparing a working and failing session is also a strong diagnostic method and helps isolate which session attributes differ, but it is slightly less direct than inspecting the server-side policy first. Restarting the service may temporarily change behavior without explaining it. Manual addressing is a workaround.",
            "shorthand": "Network Issue",
            "longhand": "VPN assigns incorrect IP range blocking access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_storage_008",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 42,
            "question": "A file server loses a large amount of disk space overnight, and users also report unusual file renames. What is the best first response?",
            "choices": [
                {
                    "answerText": "Investigate the file activity immediately and escalate the event as a possible active incident before normal cleanup actions",
                    "score": 42
                },
                {
                    "answerText": "Place the share in a limited-access state and collect recent file-change details so you can determine whether automation or malware is responsible",
                    "score": 36
                },
                {
                    "answerText": "Expand the volume temporarily so service remains available while you review the changed data afterward",
                    "score": 18
                },
                {
                    "answerText": "Delete the newest large files first so the volume returns to normal and then revisit the renames later",
                    "score": 7
                }
            ],
            "feedback": "The strongest first response is to treat the combination of sudden space loss and unusual renames as potentially malicious and investigate immediately. Restricting access and collecting change data is also a strong containment-oriented response, but it is slightly more tactical than the broader incident-first framing. Expanding storage may keep service alive but does not address the apparent abnormal activity. Deleting files can remove evidence or worsen impact.",
            "shorthand": "Software Issue",
            "longhand": "Sudden disk loss with suspicious file renames",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_gpo_009",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 40,
            "question": "After a new Group Policy deployment, many machines become noticeably slower during login and startup. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Review the newly deployed policy settings and identify which recent change aligns with the slowdown pattern",
                    "score": 40
                },
                {
                    "answerText": "Compare one affected machine and one unaffected machine with policy-result data to isolate which setting is adding delay",
                    "score": 33
                },
                {
                    "answerText": "Restart the impacted machines and see whether the next boot applies the policy more cleanly",
                    "score": 13
                },
                {
                    "answerText": "Disable unrelated background software globally to reduce boot-time overhead while the issue is present",
                    "score": 7
                }
            ],
            "feedback": "Reviewing the changed policy itself is the strongest first step because the slowdown appeared directly after deployment. Comparing affected and unaffected machines is also strong and can isolate the exact setting, but it follows naturally after acknowledging that the recent policy change is the likely source. Restarting repeats the same condition without diagnosis. Disabling unrelated software is too speculative.",
            "shorthand": "Software Issue",
            "longhand": "New group policy causing widespread login slowdown",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_service_010",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 41,
            "question": "An internal application service shows as running, but clients cannot connect and port tests fail. What is the best first step?",
            "choices": [
                {
                    "answerText": "Verify whether the service is truly listening on the expected interface and whether firewalls allow the connection path",
                    "score": 41
                },
                {
                    "answerText": "Compare local service port state to a known-good server running the same application stack",
                    "score": 34
                },
                {
                    "answerText": "Restart the service and check whether the port binds properly after a clean startup cycle",
                    "score": 14
                },
                {
                    "answerText": "Reinstall the clients that are reporting connection failures to eliminate workstation-side variables",
                    "score": 6
                }
            ],
            "feedback": "Confirming whether the service is actually listening and reachable is the strongest first step because the failure appears before the application layer fully engages. Comparing against a known-good server is also a strong diagnostic method, but it is slightly less direct than checking the affected service's port and firewall state. Restarting the service may help if binding failed, but it is still a change before diagnosis. Reinstalling clients is weaker.",
            "shorthand": "Software Issue",
            "longhand": "Service running but not accepting connections",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_proxy_011",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 43,
            "question": "After a firewall policy change, users can reach some external sites but fail on others in inconsistent ways. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the changed firewall, proxy, or filtering logic and map the failures to the new outbound policy behavior",
                    "score": 43
                },
                {
                    "answerText": "Run controlled browsing tests from multiple users and compare the failing destinations against category, protocol, or path differences",
                    "score": 35
                },
                {
                    "answerText": "Clear browser caches and authentication tokens on the most heavily impacted user machines",
                    "score": 9
                },
                {
                    "answerText": "Roll back the browser version on the affected workstations to rule out client rendering regressions",
                    "score": 7
                }
            ],
            "feedback": "The strongest first move is to connect the symptom pattern to the known firewall change. Controlled browsing tests are also strong and help isolate scope and traffic class, but they complement rather than replace checking the changed policy. Cache clearing and browser rollback are weaker because the issue spans users after a network-layer change.",
            "shorthand": "Network Issue",
            "longhand": "Firewall change causing inconsistent external site access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_identity_012",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 47,
            "question": "A machine reports a trust relationship failure, and other symptoms suggest the computer account password may be out of sync with the domain. What is the best response?",
            "choices": [
                {
                    "answerText": "Repair the machine account trust or reset the secure channel after confirming the trust path is broken",
                    "score": 47
                },
                {
                    "answerText": "Validate secure channel status and domain reachability first, then decide whether the machine account needs repair",
                    "score": 39
                },
                {
                    "answerText": "Create a fresh user profile so the user can sign in under a newly built desktop context",
                    "score": 8
                },
                {
                    "answerText": "Shift the user to a permanent local account so work can continue without domain dependency",
                    "score": 5
                }
            ],
            "feedback": "Repairing the machine trust is the strongest corrective action when the machine account relationship is the real failure. Validating the secure channel first is also a very strong answer because it confirms the diagnosis before altering the relationship, but it is slightly less direct as the response. Creating a new user profile does not fix machine trust. Permanent local-account use avoids the problem rather than solving it.",
            "shorthand": "Device Issue",
            "longhand": "Machine trust relationship failure with domain",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_dns_013",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 44,
            "question": "Internal domains resolve correctly, but external domains fail from the DNS servers themselves. What should you check first?",
            "choices": [
                {
                    "answerText": "Review DNS forwarders, root hints, and whether the servers have working outbound DNS reachability",
                    "score": 44
                },
                {
                    "answerText": "Query several external names directly from the DNS servers and compare responses by forwarder path to isolate where resolution stops",
                    "score": 35
                },
                {
                    "answerText": "Point clients to public DNS temporarily so internet name resolution can continue while you investigate",
                    "score": 15
                },
                {
                    "answerText": "Restart the DNS service and wait for it to rebuild normal external resolution behavior",
                    "score": 12
                }
            ],
            "feedback": "Checking forwarders, root hints, and outbound reachability is the strongest first step because internal resolution still works, which narrows the failure to external lookup handling. Direct query testing from the servers is also strong and helps isolate the break point, but it follows the same root hypothesis. Pointing clients elsewhere may restore some access temporarily, yet it bypasses the issue and can break internal resolution design. Restarting DNS is broader and less informative.",
            "shorthand": "Access Issue",
            "longhand": "Internal DNS works, external resolution failing",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_forensics_014",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 49,
            "question": "A workstation shows an unknown process and unusual outbound traffic spikes to destinations users do not recognize. What is the best first action?",
            "choices": [
                {
                    "answerText": "Isolate the workstation from the network and escalate while preserving as much investigative context as possible",
                    "score": 49
                },
                {
                    "answerText": "Capture the current connection and process details immediately before deciding whether to isolate the system",
                    "score": 37
                },
                {
                    "answerText": "Kill the suspicious process and monitor whether the traffic pattern stops without disconnecting the machine",
                    "score": 20
                },
                {
                    "answerText": "Restart the system and return it to the user if the traffic does not reappear right away",
                    "score": 8
                }
            ],
            "feedback": "Isolation with escalation is strongest because suspicious outbound behavior can indicate compromise and active harm to the environment. Capturing connection and process details first is also a strong option if done quickly and safely, but it introduces some delay before containment. Killing the process may reduce symptoms while destroying useful evidence. Restarting can also erase context and is weaker.",
            "shorthand": "Network Issue",
            "longhand": "Unknown process causing abnormal outbound traffic spikes",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_cert_015",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 42,
            "question": "An internal application suddenly begins showing certificate warnings across many systems after a certificate renewal. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the renewed certificate's binding, hostname match, and full trust chain as presented by the application",
                    "score": 42
                },
                {
                    "answerText": "Compare the old and new certificates to determine whether EKU, SAN, issuer chain, or binding behavior changed unexpectedly",
                    "score": 34
                },
                {
                    "answerText": "Restart the application service so the new certificate presentation path is fully refreshed",
                    "score": 14
                },
                {
                    "answerText": "Advise users to bypass the warning until the certificate environment stabilizes after renewal",
                    "score": 2
                }
            ],
            "feedback": "The strongest first step is to verify what certificate is actually being presented and whether it matches trust and hostname expectations. Comparing old and new certificates is also a very strong diagnostic action, but it follows after confirming the current live presentation path. Restarting the service may help if the binding was not refreshed, but it is less precise than checking the certificate state directly. Bypassing warnings is unsafe.",
            "shorthand": "Software Issue",
            "longhand": "Certificate renewal causing widespread trust warnings",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sched_016",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 40,
            "question": "An overnight scheduled task that updates shared data stops running after a service account password change. The script still works when launched manually by an admin. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the scheduled task credentials, execution context, and permission model tied to the service account change",
                    "score": 40
                },
                {
                    "answerText": "Clone the scheduled task under a separate account and compare whether the failure follows the task definition or the account context",
                    "score": 31
                },
                {
                    "answerText": "Restart the server and allow the task to retry under a clean system state on the next run",
                    "score": 11
                },
                {
                    "answerText": "Run the script manually each morning until the scheduled copy begins working again",
                    "score": 9
                }
            ],
            "feedback": "Checking the stored credentials and execution context is the strongest answer because the failure began immediately after a service account password change. Cloning the task under another account is a strong diagnostic technique, but it is a change rather than a first inspection. Restarting the server does not directly address the credential mismatch. Manual daily execution is only a workaround.",
            "shorthand": "Account Issue",
            "longhand": "Scheduled task failing after service account change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_mail_017",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 41,
            "question": "Outbound mail is delayed for all users, and queue monitoring shows messages accumulating faster than they leave. What should you do first?",
            "choices": [
                {
                    "answerText": "Review transport queue behavior, connector health, and the stage at which outbound delivery is backing up",
                    "score": 41
                },
                {
                    "answerText": "Send controlled internal-to-external tests and compare queue growth patterns by destination domain and message size",
                    "score": 33
                },
                {
                    "answerText": "Flush or clear selected queue items to see whether the transport backlog begins moving again",
                    "score": 12
                },
                {
                    "answerText": "Restart mail clients and have users resend delayed messages from scratch",
                    "score": 5
                }
            ],
            "feedback": "The strongest answer examines the transport layer directly because queue growth shows the failure is server-side. Controlled test messages are also strong and help isolate where delivery breaks, but they come after or alongside checking the queue stage itself. Clearing queue items is risky and may destroy messages without fixing the cause. Restarting clients is a weak fit.",
            "shorthand": "Network Issue",
            "longhand": "Mail queue buildup causing delivery delays",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
                "id": "hard_replication_018",
                "question_difficulty": "Hard",
                "spawn_rules": {
                    "easy": {"allowed": False, "weight": 0},
                    "medium": {"allowed": True, "weight": 4},
                    "hard": {"allowed": True, "weight": 9}
                },
                "location": defineHelpDesk,
                "points": 46,
                "question": "SYSVOL changes are visible on one domain controller but not another, and login scripts are inconsistent between sites. What should you check first?",
                "choices": [
                    {
                        "answerText": "Review SYSVOL or DFS replication health and confirm the replication path between the relevant domain controllers",
                        "score": 46
                    },
                    {
                        "answerText": "Compare the script versions and timestamps on both controllers to determine whether the issue is truly replication or an update path mistake",
                        "score": 36
                    },
                    {
                        "answerText": "Copy the correct scripts manually to the missing controller so logins become consistent again while you continue checking",
                        "score": 15
                    },
                    {
                        "answerText": "Restart the affected client machines so they redraw the latest login resources from the domain",
                        "score": 6
                    }
                ],
                "feedback": "Checking SYSVOL or DFS replication health is the strongest first step because the same domain content is inconsistent between controllers. Comparing file versions on both sides is also a strong diagnostic move and helps confirm whether replication is actually at fault, but it is slightly less direct than checking replication health itself. Manual copying can restore function but risks obscuring the root problem. Client restarts do not solve inconsistent SYSVOL content.",
                "shorthand": "Access Issue",
            "longhand": "SYSVOL replication failure causing inconsistent scripts",
                "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
                "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_latency_019",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 40,
            "question": "An application performs normally internally but becomes unusably slow for remote VPN users during peak hours only. What should you check first?",
            "choices": [
                {
                    "answerText": "Review VPN throughput, latency, and peak-time path congestion between remote users and the application environment",
                    "score": 40
                },
                {
                    "answerText": "Compare application response timing from an internal host and a VPN-connected host during the same window to separate app delay from network delay",
                    "score": 32
                },
                {
                    "answerText": "Increase server-side application resources and monitor whether remote users improve during the next peak period",
                    "score": 14
                },
                {
                    "answerText": "Schedule a daily VPN service restart before peak hours so the tunnel environment begins from a clean state",
                    "score": 9
                }
            ],
            "feedback": "Because only remote VPN users slow down and only during peak periods, the strongest first move is to inspect the VPN path and congestion profile. Internal versus VPN timing comparison is also a strong diagnostic step and helps prove whether the bottleneck is network or application, but it slightly follows the network-path hypothesis rather than replacing it. Increasing server resources may help if the application is borderline, but it does not fit the scope as well. Routine service restarts are a weak workaround.",
            "shorthand": "Network Issue",
            "longhand": "VPN users experience latency during peak hours",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_acl_020",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 45,
            "question": "After a network redesign, one subnet can reach the internet but cannot access specific internal application ports used by a legacy service. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the ACLs, firewall rules, and route changes affecting the redesigned subnet's path to the legacy service",
                    "score": 45
                },
                {
                    "answerText": "Test the legacy ports from the affected subnet and a working subnet to identify whether the loss is policy-specific or route-specific",
                    "score": 36
                },
                {
                    "answerText": "Move the affected users to a temporary VLAN that still has the older access behavior while you observe traffic patterns",
                    "score": 15
                },
                {
                    "answerText": "Reinstall the client application used to reach the service on several failing systems",
                    "score": 6
                }
            ],
            "feedback": "The strongest first step is to inspect the network policy and route changes introduced by the redesign. Comparing port access from working and failing subnets is also a strong diagnostic move and helps prove whether the failure is tied to policy or routing, but it follows the same root hypothesis. Moving users to another VLAN can restore function temporarily, though it avoids fixing the design. Reinstalling the client is weak because the symptom follows subnet placement.",
            "shorthand": "Software Issue",
            "longhand": "Subnet cannot access internal service ports",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_db_021",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 44,
            "question": "An application server can reach its database by IP, but the application still fails to authenticate after a recent service migration. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the connection string, service account permissions, and any name-based authentication dependencies introduced by the migration",
                    "score": 44
                },
                {
                    "answerText": "Compare the migrated server's application settings to the pre-migration environment to isolate which identity or endpoint detail changed",
                    "score": 35
                },
                {
                    "answerText": "Restart the database service and the application service together so the session and identity path reinitialize cleanly",
                    "score": 12
                },
                {
                    "answerText": "Replace hostname references with raw IP references everywhere in the application configuration and retest",
                    "score": 10
                }
            ],
            "feedback": "If the server can reach the database by IP but authentication fails after migration, the strongest first step is to review how the application now identifies and authenticates to the database. Comparing migrated and pre-migration settings is also a strong method and helps surface exactly what changed, but it is slightly broader than checking the live connection and identity configuration first. Restarting services may clear state but does not diagnose the migration-related difference. Replacing hostnames with IPs may bypass some name-based issues but can break intended authentication behavior.",
            "shorthand": "Software Issue",
            "longhand": "Application fails authentication after service migration",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_eventlog_022",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 40,
            "question": "A critical service began failing after a system patch cycle, but only on one of several identically configured servers. What should you check first?",
            "choices": [
                {
                    "answerText": "Compare logs, service state, and effective configuration between the failing server and a working peer",
                    "score": 40
                },
                {
                    "answerText": "Review the exact patch and application sequence on the failing host to determine whether one server diverged during the cycle",
                    "score": 34
                },
                {
                    "answerText": "Roll back the most recent patch from the failing server before collecting any additional diagnostics",
                    "score": 16
                },
                {
                    "answerText": "Restart the service several times across the patch window to see whether it stabilizes as dependencies settle",
                    "score": 10
                }
            ],
            "feedback": "Comparing the failing server to a working peer is the strongest first move because the environment should be the same except for whatever diverged. Reviewing patch sequence on the failing host is also strong and may reveal the divergence, but it is slightly narrower than side-by-side comparison of overall state. Rolling back immediately can help if a patch is the cause, yet it changes the system before diagnosis. Repeated restarts are weaker.",
            "shorthand": "Network Issue",
            "longhand": "Service failure on one patched server only",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_storage_023",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": defineHelpDesk,
            "points": 43,
            "question": "A shared storage volume is online, but only some application servers can write to it after a permission model change. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the volume ACLs, host access rules, and the service identities used by the servers that can and cannot write",
                    "score": 43
                },
                {
                    "answerText": "Compare a working application server and a failing one to determine whether the permission issue follows the host, service identity, or storage path",
                    "score": 35
                },
                {
                    "answerText": "Remove the write restrictions temporarily and observe whether all servers resume normal operation immediately",
                    "score": 12
                },
                {
                    "answerText": "Restart the storage-connected application servers to refresh any stale access tokens or sessions",
                    "score": 11
                }
            ],
            "feedback": "The strongest first step is to inspect the actual permission and identity model that changed. Comparing a working and failing server is also a strong diagnostic move and can quickly narrow whether the problem is host-specific or identity-specific, but it follows the same root direction. Temporarily removing restrictions restores access at the expense of control and can weaken security. Restarts may refresh tokens but do not explain why only some servers fail.",
            "shorthand": "Device Issue",
            "longhand": "Storage permissions inconsistent across application servers",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_cloudsync_024",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 8}
            },
            "location": defineHelpDesk,
            "points": 41,
            "question": "A hybrid identity sync job completes, but some new on-prem changes never appear in the cloud directory. What should you investigate first?",
            "choices": [
                {
                    "answerText": "Review sync scope, connector state, filtering rules, and the error path for the objects that are missing",
                    "score": 41
                },
                {
                    "answerText": "Compare one object that synced successfully and one that did not to identify which attribute or scope difference is blocking export",
                    "score": 34
                },
                {
                    "answerText": "Restart the sync server and run another full sync cycle before checking the connector details",
                    "score": 14
                },
                {
                    "answerText": "Create the missing cloud-side objects manually so the environments look aligned again",
                    "score": 10
                }
            ],
            "feedback": "Checking sync scope, filters, and object-specific errors is the strongest first move because only some changes are missing. Comparing a working and missing object is also a strong method and helps isolate the exact differentiator, but it usually follows the connector and filter review. Restarting and forcing another sync may eventually help but does not explain the selective failure. Manual cloud creation risks divergence.",
            "shorthand": "Access Issue",
            "longhand": "Hybrid sync missing some directory changes",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_cert_025",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineHelpDesk,
            "points": 48,
            "question": "Mutual TLS authentication suddenly fails between two internal services after a certificate rollover, even though both services are up and reachable. What should you check first?",
            "choices": [
                {
                    "answerText": "Review the new certificates, trust chain, mapping rules, and client or server certificate requirements used in the mutual TLS flow",
                    "score": 48
                },
                {
                    "answerText": "Compare the old and new certificates for SAN, EKU, issuer, and trust differences that could change how the two services validate one another",
                    "score": 39
                },
                {
                    "answerText": "Restart both services so the renewed certificates are reloaded from a clean state and then retest authentication",
                    "score": 15
                },
                {
                    "answerText": "Disable strict certificate validation temporarily so traffic can resume while the trust relationship is reviewed",
                    "score": 4
                }
            ],
            "feedback": "The strongest answer checks the live certificate trust and mapping requirements actually used by the mutual TLS exchange. Comparing old and new certificates is also a strong diagnostic approach and may reveal what changed, but it follows slightly behind checking the currently active certificate and trust path first. Restarting services may be appropriate if certificates were not reloaded, but it is less direct than verifying the trust requirements. Disabling validation undermines the whole security model.",
            "shorthand": "Network Issue",
            "longhand": "Mutual TLS authentication failure after certificate rollover",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_001",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "A user reports that a website is down, but only says it is not loading in their browser. What do you do first?",
            "choices": [
                {
                    "answerText": "Check whether the site fails for other users and confirm whether the issue is browser-specific or broader",
                    "score": 6
                },
                {
                    "answerText": "Clear the user's browser cache and assume the issue is just stale local content",
                    "score": 0
                },
                {
                    "answerText": "Reinstall the browser immediately because it is the fastest way to rule out client corruption",
                    "score": -5
                }
            ],
            "feedback": "The trap is assuming a browser symptom always means a browser problem. Confirming scope first avoids wasting time on a client-only fix when the issue could be broader. Clearing cache may help, but it skips validation. Reinstalling the browser commits too early to the wrong layer.",
            "shorthand": "Network Issue",
            "longhand": "Website appears down but scope not confirmed",
            "followup_event": {"allowed": True, "event_id": "trap_easy_001_followup", "score_cutoff": 6},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_001_followup",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You focused on the browser, but more users are now reporting the same website issue. How do you recover?",
            "choices": [
                {
                    "answerText": "Check DNS and upstream connectivity, then compare results from multiple users and systems",
                    "score": 0
                },
                {
                    "answerText": "Restart the affected users' computers so they can reconnect with clean sessions",
                    "score": -3
                },
                {
                    "answerText": "Continue rebuilding browsers because the first repair may not have fully completed",
                    "score": -8
                }
            ],
            "feedback": "Once the scope widens, the best recovery is to move away from the client-only assumption and check shared infrastructure. Restarting clients may produce temporary relief in a few cases, but it still does not address the likely cause. Continuing browser rebuilds deepens the mistake.",
            "shorthand": "Network Issue",
            "longhand": "Issue expands after incorrect browser-focused troubleshooting",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_easy_002",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A user says they cannot log in after a password change. What do you do first?",
            "choices": [
                {
                    "answerText": "Confirm whether old credentials are still cached on another device or service before changing the account again",
                    "score": 7
                },
                {
                    "answerText": "Reset the password again right away so the user has a fresh credential to try",
                    "score": 0
                },
                {
                    "answerText": "Disable the account until the login behavior settles down across the environment",
                    "score": -6
                }
            ],
            "feedback": "The trap is thinking every login issue after a password change needs another reset. Cached credentials on phones, VPNs, or background apps often create repeated failures. A second reset may help briefly, but it usually avoids the real cause. Disabling the account is an overreaction.",
            "shorthand": "Network Issue",
            "longhand": "Login failure misattributed to password issue",
            "followup_event": {"allowed": True, "event_id": "trap_easy_002_followup", "score_cutoff": 7},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_002_followup",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You reset the password again, but the account keeps locking out. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Trace saved credentials, synced devices, and background sign-ins still attempting the old password",
                    "score": 0
                },
                {
                    "answerText": "Keep unlocking the account as each lockout occurs so the user can continue working",
                    "score": -4
                },
                {
                    "answerText": "Create a brand-new user account and migrate access instead of investigating the lockout source",
                    "score": -9
                }
            ],
            "feedback": "The correct recovery is to find what is still using the old password. Repeated unlocks only manage the symptom. Replacing the user account causes unnecessary disruption and still avoids root cause analysis.",
            "shorthand": "Access Issue",
            "longhand": "Account lockouts persist after repeated password resets",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_easy_003",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpDesk,
            "points": 6,
            "question": "One user says a printer is not working. What do you do first?",
            "choices": [
                {
                    "answerText": "Confirm the selected printer, queue target, and whether the issue affects only that user or multiple users",
                    "score": 6
                },
                {
                    "answerText": "Restart the shared printer immediately so any stuck state is cleared before more users are affected",
                    "score": 0
                },
                {
                    "answerText": "Replace the print driver on the server before checking whether the problem is only local to one user",
                    "score": -5
                }
            ],
            "feedback": "The trap is escalating too quickly from a single-user symptom to shared infrastructure changes. Checking scope and printer selection is the strongest first step. Restarting the printer may help sometimes, but it assumes the issue is shared hardware. Replacing drivers is broader than the evidence supports.",
            "shorthand": "Software Issue",
            "longhand": "Single user printer issue escalated too quickly",
            "followup_event": {"allowed": True, "event_id": "trap_easy_003_followup", "score_cutoff": 6},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_003_followup",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You restarted the shared printer, but now other users are complaining too. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Check the shared queue, verify the user's target printer, and compare behavior between working and failing users",
                    "score": 0
                },
                {
                    "answerText": "Restart the print server as well so the whole path reinitializes together",
                    "score": -4
                },
                {
                    "answerText": "Redeploy the printer to every user immediately to eliminate any remaining client inconsistency",
                    "score": -8
                }
            ],
            "feedback": "The best way out is to return to scope and queue analysis. Restarting more infrastructure expands the disruption without proving the cause. Full redeployment is even more disruptive and still does not confirm whether the original issue was local.",
            "shorthand": "Network Issue",
            "longhand": "Restart caused wider printer outage across users",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_easy_004",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpDesk,
            "points": 8,
            "question": "A user says they lost access after changing roles. What do you do first?",
            "choices": [
                {
                    "answerText": "Compare current group membership with the access model expected for the new role",
                    "score": 8
                },
                {
                    "answerText": "Grant the requested access manually so the user can keep working while role mapping is checked later",
                    "score": 0
                },
                {
                    "answerText": "Clone access from another employee with a similar title so the permissions match more quickly",
                    "score": -7
                }
            ],
            "feedback": "The trap is solving the access symptom without validating the role model. Group membership is the correct first place to look. Manual granting may get the user working, but it bypasses intended controls. Cloning someone else's access can over-permission the user badly.",
            "shorthand": "Network Issue",
            "longhand": "Access issue solved without validating role model",
            "followup_event": {"allowed": True, "event_id": "trap_easy_004_followup", "score_cutoff": 8},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_004_followup",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You granted access manually, and now the user can reach resources their new role should not have. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Remove the manual grants, verify role-based groups, and reapply only the access required by the role model",
                    "score": 0
                },
                {
                    "answerText": "Leave the access in place for now and document the exception until someone else reviews the role mapping",
                    "score": -5
                },
                {
                    "answerText": "Copy the same manual access to similar users so the department stays consistent",
                    "score": -10
                }
            ],
            "feedback": "The best recovery is to undo the manual shortcut and return to the intended access structure. Leaving excess access in place preserves the security problem. Expanding the same mistake to more users makes the damage worse.",
            "shorthand": "Software Issue",
            "longhand": "Manual access caused over-permission security risk",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_easy_005",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpDesk,
            "points": 7,
            "question": "A workstation is very slow and memory usage is almost full. What do you do first?",
            "choices": [
                {
                    "answerText": "Identify the memory-heavy processes before deciding whether the issue is normal load or a runaway application",
                    "score": 7
                },
                {
                    "answerText": "Restart the PC immediately so the user gets temporary relief while you plan a deeper review later",
                    "score": 0
                },
                {
                    "answerText": "Recommend replacing the workstation because high memory use usually means the hardware is no longer sufficient",
                    "score": -6
                }
            ],
            "feedback": "The trap is jumping to relief or replacement before understanding the memory load. Restarting may help briefly, but it erases useful context. Replacement assumes the problem is hardware when it may be a single bad process.",
            "shorthand": "Software Issue",
            "longhand": "Slow system assumed hardware instead of process",
            "followup_event": {"allowed": True, "event_id": "trap_easy_005_followup", "score_cutoff": 7},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_easy_005_followup",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You restarted the PC, but the slowdown returned after logon. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Inspect process memory usage, startup behavior, and whether a specific app is reclaiming all available memory",
                    "score": 0
                },
                {
                    "answerText": "Schedule another restart later in the day so the user gets several shorter windows of normal performance",
                    "score": -4
                },
                {
                    "answerText": "Begin replacing hardware immediately without collecting any application or process data",
                    "score": -9
                }
            ],
            "feedback": "Once the slowdown returns, the right recovery is to inspect what is consuming memory. Repeated restarts only hide the issue temporarily. Replacing hardware without evidence can waste time and still miss the true cause.",
            "shorthand": "Network Issue",
            "longhand": "Performance issue returns after temporary restart fix",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_medium_001",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 22,
            "question": "A new Group Policy is applying to some users but not others in the same department. What do you do first?",
            "choices": [
                {
                    "answerText": "Check OU placement, inheritance, and filtering before changing machines or domain infrastructure",
                    "score": 22
                },
                {
                    "answerText": "Run gpupdate on affected users and assume any policy gap is just a delayed refresh problem",
                    "score": 0
                },
                {
                    "answerText": "Restart the domain controller that received the latest policy edits to clear possible stale policy state",
                    "score": -18
                }
            ],
            "feedback": "The trap is assuming inconsistency means policy refresh rather than policy scope. Checking targeting is the strongest answer. Forcing updates can help test symptoms, but it does not prove the policy is scoped correctly. Restarting a domain controller is disruptive and poorly targeted.",
            "shorthand": "Device Issue",
            "longhand": "Group policy issue mistaken for refresh delay",
            "followup_event": {"allowed": True, "event_id": "trap_medium_001_followup", "score_cutoff": 22},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_medium_001_followup",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You forced policy updates, but the same users still do not receive the new setting. How do you recover?",
            "choices": [
                {
                    "answerText": "Compare a working user and a failing user for OU location, inheritance, and filtering differences",
                    "score": 0
                },
                {
                    "answerText": "Continue forcing updates and have the users log off repeatedly until the setting eventually appears",
                    "score": -11
                },
                {
                    "answerText": "Duplicate the policy into a second GPO and link it broadly so it reaches everyone by force",
                    "score": -26
                }
            ],
            "feedback": "The best recovery is to compare scope and policy path between working and failing users. Repeated gpupdate cycles continue the same wrong assumption. Broadly duplicating the policy can create even more confusion and side effects.",
            "shorthand": "Access Issue",
            "longhand": "Policy still fails due to incorrect scope assumptions",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_medium_002",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 21,
            "question": "Several users report Outlook credential prompts, but other services still authenticate normally. What do you do first?",
            "choices": [
                {
                    "answerText": "Check cached credentials, profile state, and whether the mail endpoint configuration still matches expectations",
                    "score": 21
                },
                {
                    "answerText": "Reset the affected passwords so every user gets a fresh authentication path into the mailbox service",
                    "score": 0
                },
                {
                    "answerText": "Reinstall Office on all affected systems so the client stack is rebuilt the same way everywhere",
                    "score": -17
                }
            ],
            "feedback": "The trap is treating a mail-specific prompt as a general credential failure. Checking cached credentials and profile state matches the actual scope of the issue. Password resets may work in a few cases, but they skip the more likely cause. Reinstalling Office across affected systems is an unnecessarily broad move.",
            "shorthand": "Network Issue",
            "longhand": "Outlook prompts mistaken for credential failure",
            "followup_event": {"allowed": True, "event_id": "trap_medium_002_followup", "score_cutoff": 21},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_medium_002_followup",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You reset passwords, but Outlook still prompts on the same users. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Inspect cached credentials, rebuild one mail profile if needed, and compare the result against the existing configuration",
                    "score": 0
                },
                {
                    "answerText": "Reset the passwords again and clear every remembered login so no old token remains anywhere",
                    "score": -10
                },
                {
                    "answerText": "Continue reimaging or reinstalling office applications until the prompts disappear on at least one machine",
                    "score": -24
                }
            ],
            "feedback": "The correct recovery is to move back toward cached credentials and profile state. Repeating password resets extends the same mistake. Broad rebuilds add more disruption while still avoiding the likely cause.",
            "shorthand": "Software Issue",
            "longhand": "Credential prompts persist after unnecessary resets",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_medium_003",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 23,
            "question": "A shared folder is accessible to some users, but others get access denied even though they should match. What do you do first?",
            "choices": [
                {
                    "answerText": "Compare permissions and group membership between a working user and a failing user before granting anything new",
                    "score": 23
                },
                {
                    "answerText": "Grant the affected users direct access temporarily so work continues while you investigate later",
                    "score": 0
                },
                {
                    "answerText": "Restart the file server to refresh file-sharing behavior and clear any stale access state",
                    "score": -16
                }
            ],
            "feedback": "The trap is bypassing permission analysis with temporary grants. Comparing a working user to a failing user reveals the access difference cleanly. Direct grants may solve the symptom but damage the permission model. Restarting the server does not fit an authorization problem well.",
            "shorthand": "Software Issue",
            "longhand": "Access denied solved by bypassing permissions",
            "followup_event": {"allowed": True, "event_id": "trap_medium_003_followup", "score_cutoff": 23},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_medium_003_followup",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You granted direct access, and now the folder has inconsistent permissions across users. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Remove the temporary grants and reconcile the permission model using group membership and intended share design",
                    "score": 0
                },
                {
                    "answerText": "Leave the direct permissions in place and document the exceptions so no one loses access again",
                    "score": -12
                },
                {
                    "answerText": "Expand the direct permissions to similar users so the share behaves the same way for the whole team",
                    "score": -27
                }
            ],
            "feedback": "The best way out is to remove the shortcut and restore the intended permission design. Leaving exceptions in place preserves the problem. Expanding the mistake to more users creates a much larger access-control issue.",
            "shorthand": "Network Issue",
            "longhand": "Permission inconsistencies caused by manual overrides",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_medium_004",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 24,
            "question": "A Windows service starts, then immediately stops. What do you do first?",
            "choices": [
                {
                    "answerText": "Check dependencies, startup parameters, and event log details before changing the service configuration",
                    "score": 24
                },
                {
                    "answerText": "Change the service account first so the process has a different identity and may stay running",
                    "score": 0
                },
                {
                    "answerText": "Restart the whole server so the service has a cleaner startup sequence and more room to stabilize",
                    "score": -18
                }
            ],
            "feedback": "The trap is making service changes before understanding why the service stops. Logs and dependencies are the strongest first step. Changing the account can help sometimes, but it changes a variable before diagnosis. Restarting the server is broader and less informative.",
            "shorthand": "Device Issue",
            "longhand": "Service failure fixed without checking logs",
            "followup_event": {"allowed": True, "event_id": "trap_medium_004_followup", "score_cutoff": 24},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_medium_004_followup",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You changed the service account, but the service still starts and stops. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Return to the logs, dependency chain, and startup configuration to identify the actual reason for the stop event",
                    "score": 0
                },
                {
                    "answerText": "Try additional service accounts until one of them appears to keep the service running longer",
                    "score": -12
                },
                {
                    "answerText": "Rebuild the server role entirely so the service can be reintroduced in a clean environment",
                    "score": -28
                }
            ],
            "feedback": "The correct recovery is to go back to evidence from logs and dependencies. Cycling through more service accounts repeats the same guesswork. Rebuilding the whole server is a major escalation without diagnosis.",
            "shorthand": "Access Issue",
            "longhand": "Service still failing due to missed root cause",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_medium_005",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 2}
            },
            "location": defineHelpDesk,
            "points": 25,
            "question": "Backups report success, but restore tests fail. What do you do first?",
            "choices": [
                {
                    "answerText": "Inspect backup logs, restore settings, and chain integrity to confirm whether the backups are actually usable",
                    "score": 25
                },
                {
                    "answerText": "Run another backup cycle first so you have a newer set before continuing the restore investigation",
                    "score": 0
                },
                {
                    "answerText": "Delete the current backup set and build a fresh schedule because the old one is clearly unreliable now",
                    "score": -20
                }
            ],
            "feedback": "The trap is trusting job success messages more than restore evidence. The strongest move is to inspect why restore use is failing. Running another backup does not fix a broken restore path. Deleting the backup set can remove data you may still need.",
            "shorthand": "Network Issue",
            "longhand": "Backup success assumed without restore validation",
            "followup_event": {"allowed": True, "event_id": "trap_medium_005_followup", "score_cutoff": 25},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_medium_005_followup",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You ran another backup, but restore tests still fail. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Compare restore behavior across multiple restore points and inspect the backup chain and restore configuration directly",
                    "score": 0
                },
                {
                    "answerText": "Continue running fresh backups until one of them eventually restores correctly",
                    "score": -13
                },
                {
                    "answerText": "Stop doing restore tests and rely on successful backup job status until a real emergency happens",
                    "score": -30
                }
            ],
            "feedback": "The only good recovery is to focus on restore function itself. More backups can continue failing silently. Abandoning restore testing is the worst outcome because it leaves recovery capability unknown.",
            "shorthand": "Software Issue",
            "longhand": "Restore failure persists despite new backups",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_001",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineHelpDesk,
            "points": 44,
            "question": "Users intermittently fail Kerberos authentication, and password resets do not help. What do you do first?",
            "choices": [
                {
                    "answerText": "Check time synchronization and DNS paths between clients and the domain controllers involved in the failures",
                    "score": 44
                },
                {
                    "answerText": "Capture more failed sign-ins before touching the environment so you can build a cleaner pattern of the incident",
                    "score": 0
                },
                {
                    "answerText": "Restart the affected domain controllers so authentication starts from a clean service state",
                    "score": -34
                }
            ],
            "feedback": "The trap is delaying or overreacting instead of validating Kerberos fundamentals first. Time and DNS are directly tied to Kerberos success. Collecting more failure data can be useful, but it delays the most likely root checks. Restarting domain controllers is disruptive and does not target the most probable cause.",
            "shorthand": "Software Issue",
            "longhand": "Kerberos failures misdiagnosed without checking dependencies",
            "followup_event": {"allowed": True, "event_id": "trap_hard_001_followup", "score_cutoff": 44},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_hard_001_followup",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You restarted domain controllers, but Kerberos failures continue and users are now more disrupted. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Check time skew, DNS resolution, and which controllers the failing clients are actually reaching",
                    "score": 0
                },
                {
                    "answerText": "Restart more affected systems so every authentication component comes back up in a consistent order",
                    "score": -18
                },
                {
                    "answerText": "Disable Kerberos-related enforcement temporarily so logins can proceed while you revisit the issue later",
                    "score": -50
                }
            ],
            "feedback": "The best recovery is to return to the actual dependencies of Kerberos. More restarts only extend the disruption. Weakening authentication controls to hide the problem creates a far worse outcome.",
            "shorthand": "Network Issue",
            "longhand": "Kerberos failures persist after unnecessary restarts",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_002",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineHelpDesk,
            "points": 46,
            "question": "ARP conflicts are causing intermittent connectivity across part of the network. What do you do first?",
            "choices": [
                {
                    "answerText": "Trace the duplicate IP source and identify whether the conflict is coming from DHCP, static addressing, or a rogue device",
                    "score": 46
                },
                {
                    "answerText": "Restart the affected switches first so learned state is cleared before deeper network tracing begins",
                    "score": 0
                },
                {
                    "answerText": "Assign new static IPs to impacted users so they can reconnect while the environment stabilizes",
                    "score": -32
                }
            ],
            "feedback": "The trap is reacting to the symptom instead of finding the duplicate address source. Switch restarts may reduce symptoms briefly, but they do not solve the conflict. Assigning more static IPs can make the addressing problem worse.",
            "shorthand": "Device Issue",
            "longhand": "ARP conflict handled without identifying duplicate source",
            "followup_event": {"allowed": True, "event_id": "trap_hard_002_followup", "score_cutoff": 46},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_hard_002_followup",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You restarted switches, but the ARP conflict came back and more users are now unstable. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Identify the conflicting address owners and correct the duplicate IP assignment at the source",
                    "score": 0
                },
                {
                    "answerText": "Restart the same switches again during a quieter period so the network has a better chance to settle",
                    "score": -20
                },
                {
                    "answerText": "Begin mass readdressing users without first determining which device actually owns the duplicate IP",
                    "score": -52
                }
            ],
            "feedback": "Once the conflict returns, the only real path out is to identify the address collision source. More restarts keep repeating the same ineffective action. Mass readdressing without diagnosis risks breaking more systems than the original conflict.",
            "shorthand": "Access Issue",
            "longhand": "ARP conflicts return after ineffective switch restarts",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_003",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineHelpDesk,
            "points": 48,
            "question": "A workstation shows an unknown process and unusual outbound traffic spikes. What do you do first?",
            "choices": [
                {
                    "answerText": "Isolate the workstation from the network and escalate while preserving as much context as possible",
                    "score": 48
                },
                {
                    "answerText": "Collect more process and connection evidence before deciding whether the host really needs containment",
                    "score": 0
                },
                {
                    "answerText": "Kill the suspicious process and return the workstation to the user if the traffic stops afterward",
                    "score": -36
                }
            ],
            "feedback": "The trap is waiting too long or destroying evidence before containment. Isolation is the strongest protective response when compromise is plausible. Additional collection can be useful, but it should not delay reasonable containment. Killing the process may hide the symptom while destroying context.",
            "shorthand": "Network Issue",
            "longhand": "Suspicious activity handled without proper containment",
            "followup_event": {"allowed": True, "event_id": "trap_hard_003_followup", "score_cutoff": 48},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_hard_003_followup",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You killed the process, but the traffic resumed under a different name and evidence is now incomplete. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Isolate the host now and escalate the event with whatever connection and timeline data remains available",
                    "score": 0
                },
                {
                    "answerText": "Keep terminating suspicious processes as they appear until one of them does not come back",
                    "score": -22
                },
                {
                    "answerText": "Restart the system and release it back to the user if traffic looks normal for a few minutes",
                    "score": -54
                }
            ],
            "feedback": "Even after losing some evidence, isolation is still the best recovery step. Repeatedly terminating processes keeps damaging the investigation and may not stop the root cause. Restarting and returning the system to use risks continued compromise.",
            "shorthand": "Software Issue",
            "longhand": "Compromise worsens after destroying investigative evidence",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_004",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineHelpDesk,
            "points": 45,
            "question": "After a network redesign, one subnet can reach the internet but not a legacy internal application. What do you do first?",
            "choices": [
                {
                    "answerText": "Check ACLs, route changes, and firewall policy between the redesigned subnet and the legacy service path",
                    "score": 45
                },
                {
                    "answerText": "Move affected users temporarily to a known-working subnet so operations continue while the redesign is reviewed later",
                    "score": 0
                },
                {
                    "answerText": "Reinstall the application client on impacted systems so it can adapt to the new network environment",
                    "score": -30
                }
            ],
            "feedback": "The trap is treating a path-specific network issue like a client application problem. The strongest first step is to inspect the routing and policy path that changed. Moving users can work around the issue briefly, but it delays fixing the design. Reinstalling clients does not fit the subnet-specific symptom.",
            "shorthand": "Network Issue",
            "longhand": "Subnet access issue misdiagnosed as client problem",
            "followup_event": {"allowed": True, "event_id": "trap_hard_004_followup", "score_cutoff": 45},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_hard_004_followup",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You moved users to another subnet, but now policy exceptions are spreading and the legacy app path is still unresolved. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Return to the ACL, firewall, and route path for the affected subnet and validate the exact policy break",
                    "score": 0
                },
                {
                    "answerText": "Keep moving additional users to the working subnet so the business impact stays low while the redesign remains unchanged",
                    "score": -20
                },
                {
                    "answerText": "Redesign the client deployment package first so the application behaves the same on every subnet regardless of policy",
                    "score": -50
                }
            ],
            "feedback": "The best recovery is to fix the network path that broke. Moving more users keeps increasing operational sprawl. Reworking the client package does not address the policy and route issue that created the failure.",
            "shorthand": "Access Issue",
            "longhand": "Network issues expand due to workaround subnet moves",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_005",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 1},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineHelpDesk,
            "points": 47,
            "question": "A hybrid identity sync completes successfully, but some on-prem changes never appear in the cloud directory. What do you do first?",
            "choices": [
                {
                    "answerText": "Check sync scope, filtering, connector health, and object-specific sync errors before creating cloud-side fixes",
                    "score": 47
                },
                {
                    "answerText": "Create the missing cloud objects manually so the two environments look aligned again while you investigate later",
                    "score": 0
                },
                {
                    "answerText": "Restart the sync server and force repeated full sync cycles until every missing object eventually appears",
                    "score": -35
                }
            ],
            "feedback": "The trap is hiding a selective sync problem with manual cloud-side fixes or repeated sync retries. The strongest first step is to inspect why those objects are excluded or failing. Manual creation can create divergence. Repeated full syncs still avoid the actual filter or connector problem.",
            "shorthand": "Network Issue",
            "longhand": "Sync issue bypassed with manual cloud fixes",
            "followup_event": {"allowed": True, "event_id": "trap_hard_005_followup", "score_cutoff": 47},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "trap_hard_005_followup",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 0},
                "hard": {"allowed": True, "weight": 0}
            },
            "location": defineHelpDesk,
            "points": 0,
            "question": "You created missing cloud objects manually, but now identities are drifting between on-prem and cloud. What is the best recovery step?",
            "choices": [
                {
                    "answerText": "Identify the sync scope or filtering problem, then reconcile the manually created cloud objects with the intended sync model",
                    "score": 0
                },
                {
                    "answerText": "Continue creating missing cloud objects by hand so the visible directories stay aligned for users",
                    "score": -22
                },
                {
                    "answerText": "Disable synchronization entirely until the cloud directory is rebuilt from the manually created objects",
                    "score": -55
                }
            ],
            "feedback": "The only real recovery is to fix the sync model and then reconcile the manual drift. Continuing manual creation makes the divergence worse. Disabling synchronization entirely turns a selective sync issue into a much larger identity management failure.",
            "shorthand": "Network Issue",
            "longhand": "Directory drift caused by manual sync bypass",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        }
    ]
    return
