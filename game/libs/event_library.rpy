init python:

    event_library = [

    {
        "id": "easy_net_001",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 10},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A user says websites are not loading, but shared drives and other internal resources still work. What should you check first?",
        "choices": [
            {
                "text": "Test DNS resolution for external domains and compare it to internal name resolution",
                "score": 6
            },
            {
                "text": "Restart the workstation and retest whether external browsing returns after a clean boot",
                "score": 4
            },
            {
                "text": "Reinstall the browser and verify whether the pages load correctly afterward",
                "score": 1
            }
        ],
        "feedback": "If internal resources still work, the strongest first lead is external name resolution rather than general connectivity. Restarting the workstation can help if the issue is tied to a temporary client-side state, but it does not directly test the likely cause. Reinstalling the browser is the weakest choice because the pattern points to resolution or network behavior, not the browser itself.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_auth_002",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 10},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A user cannot sign in and gets a wrong password message. What is the best first response?",
        "choices": [
            {
                "text": "Verify keyboard input details such as caps lock, layout, and possible typing mistakes before changing the account",
                "score": 7
            },
            {
                "text": "Reset the password right away and confirm whether the account accepts the new credential",
                "score": 5
            },
            {
                "text": "Disable the account temporarily and wait for the user to try again later",
                "score": 1
            }
        ],
        "feedback": "Simple input problems are common and easy to rule out first. Resetting the password can solve the issue, but it skips a basic check and changes the account state earlier than necessary. Disabling the account is too aggressive for an ordinary sign-in failure.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_print_003",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 9},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "One user cannot print, but everyone else can. What should you check first?",
        "choices": [
            {
                "text": "Confirm that the correct printer is selected and still available on that specific user's device",
                "score": 6
            },
            {
                "text": "Restart the shared printer and test whether the user's next print job leaves the queue",
                "score": 3
            },
            {
                "text": "Replace the print driver on the server and redeploy the printer connection to users",
                "score": 1
            }
        ],
        "feedback": "Since only one user is affected, the best first check is the local printer selection or device mapping. Restarting the printer may help in some cases, but the limited scope makes a shared hardware issue less convincing. Replacing the server-side driver is broader than needed for a single-user symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_dns_004",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 10},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 8,
        "question": "A user can reach a server by IP address but not by hostname. What is the most likely issue?",
        "choices": [
            {
                "text": "The hostname is failing to resolve correctly through DNS or related name services",
                "score": 8
            },
            {
                "text": "The server is unavailable even though direct network access still appears to work",
                "score": 2
            }
        ],
        "feedback": "If the server responds by IP, the basic network path is functioning. That makes name resolution the strongest explanation. A server outage does not fit as well because direct access already succeeded.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_perf_005",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 9},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A user reports their PC is very slow, and Task Manager shows one process using 95% CPU. What should you do first?",
        "choices": [
            {
                "text": "Identify the process and determine whether it is expected, misbehaving, or suspicious before stopping it",
                "score": 7
            },
            {
                "text": "End the process immediately and watch whether overall responsiveness improves afterward",
                "score": 5
            },
            {
                "text": "Leave the process alone and continue only if the system becomes completely unusable",
                "score": 0
            }
        ],
        "feedback": "The best first move is to understand what the process is, since it could be legitimate, broken, or malicious. Ending it may improve performance quickly, but it risks interrupting something important before you know what it does. Ignoring unusually high CPU use leaves the likely cause untouched.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_time_006",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A domain user cannot log in, and the workstation clock is several minutes off. What should you do first?",
        "choices": [
            {
                "text": "Synchronize the workstation time with the domain source and retry domain authentication",
                "score": 6
            },
            {
                "text": "Reset the user's password and test whether a fresh credential resolves the sign-in failure",
                "score": 3
            },
            {
                "text": "Remove the PC from the domain and join it again to rebuild the machine relationship",
                "score": 1
            }
        ],
        "feedback": "Time mismatch is a direct problem for domain authentication, especially with Kerberos. Resetting the password changes credentials without addressing the timing issue. Rejoining the domain is much more disruptive than needed for this symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_wifi_007",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 10},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A laptop user says they cannot connect to Wi-Fi. What is the best first check?",
        "choices": [
            {
                "text": "Confirm that wireless networking is enabled on the device and that airplane mode is not active",
                "score": 5
            },
            {
                "text": "Replace the wireless router and test whether the user's connection returns afterward",
                "score": 1
            }
        ],
        "feedback": "Basic client-side state is quick to verify and often resolves the issue immediately. Replacing network hardware is far too large a first step when the problem may be local to the laptop.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_drive_008",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 9},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A user cannot access a mapped drive they normally use. What should you check first?",
        "choices": [
            {
                "text": "Verify that the path is reachable and that the user still has the permissions required for that share",
                "score": 7
            },
            {
                "text": "Restart the file server and test whether the mapped drive reconnects on the next attempt",
                "score": 3
            },
            {
                "text": "Create a replacement shared folder with the same name so the user has something to reconnect to",
                "score": 0
            }
        ],
        "feedback": "Mapped drive failures are most often tied to permissions or path reachability. Restarting the server affects everyone and is not well justified as a first check. Creating a new share does not solve the original problem and can make troubleshooting more confusing.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_mail_009",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A user's emails are stuck in the Outbox. What should you check first?",
        "choices": [
            {
                "text": "Check for a large attachment or a connectivity problem that is preventing the message from leaving",
                "score": 6
            },
            {
                "text": "Reinstall the email client and confirm whether the queue clears after the reinstall finishes",
                "score": 2
            },
            {
                "text": "Delete the user's mail profile immediately and rebuild it before doing any other testing",
                "score": 1
            }
        ],
        "feedback": "Large attachments and connection problems are common reasons mail remains in the Outbox. Reinstalling the client may help in some cases, but it is a heavier step than checking the most likely cause first. Deleting the profile immediately is riskier and skips simple validation.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_lockout_010",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 10},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 8,
        "question": "A user's account keeps locking again shortly after being unlocked. What is the best thing to investigate?",
        "choices": [
            {
                "text": "Look for saved credentials, mobile devices, or background services still trying the old password",
                "score": 8
            },
            {
                "text": "Continue unlocking the account each time it locks so the user can keep working between lockouts",
                "score": 4
            },
            {
                "text": "Delete the account and build a replacement user object with the same access permissions",
                "score": 1
            }
        ],
        "feedback": "Repeated lockouts usually mean something is still using outdated credentials in the background. Repeatedly unlocking the account only treats the symptom. Recreating the account is much more disruptive than needed for a common credential issue.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_browser_011",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A website displays incorrectly for one user, but works for others. What is a strong first step?",
        "choices": [
            {
                "text": "Clear the browser cache and reload the site to see whether the incorrect local content is replaced",
                "score": 5
            },
            {
                "text": "Restart the web server and check whether the single-user display problem disappears afterward",
                "score": 1
            }
        ],
        "feedback": "Because the issue affects one user, local browser state is a stronger suspect than the website server itself. Restarting the server is not a strong first move for a single-user display problem.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_disk_012",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A workstation is sluggish and Task Manager shows disk usage near 100%. What should you do first?",
        "choices": [
            {
                "text": "Identify which processes are driving disk activity and compare whether the load looks expected or abnormal",
                "score": 6
            },
            {
                "text": "Leave the system alone for now and only act if the workstation becomes completely unusable",
                "score": 0
            }
        ],
        "feedback": "High disk usage usually comes from a specific process or workload, so identifying the source is the strongest first move. Waiting without checking anything leaves the likely cause unresolved.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_usb_013",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": True, "weight": 3},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A USB device is not recognized when plugged in. What is the best first step?",
        "choices": [
            {
                "text": "Try another USB port and verify whether the device connection changes at the hardware level",
                "score": 5
            },
            {
                "text": "Replace the motherboard and test whether the device is detected after the hardware swap",
                "score": 0
            }
        ],
        "feedback": "Trying another port is fast, low-risk, and directly checks whether the issue is local to the port or connection. Replacing major hardware is not justified as a first troubleshooting step.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_audio_014",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": True, "weight": 3},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A user reports no sound from their computer. What should you check first?",
        "choices": [
            {
                "text": "Check the active output device and volume state to confirm audio is routed where the user expects",
                "score": 5
            },
            {
                "text": "Replace the speakers and test whether new hardware restores the missing sound path",
                "score": 2
            },
            {
                "text": "Reinstall the operating system and verify whether the rebuilt environment restores audio playback",
                "score": 0
            }
        ],
        "feedback": "Audio output selection and mute state are common causes of missing sound and are easy to verify first. Replacing speakers may help if hardware is bad, but it is not the strongest first move. Reinstalling the operating system is far too heavy for this symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_update_015",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A system update failed to install. What is the best next step?",
        "choices": [
            {
                "text": "Retry the update and review the error details or logs so the failure can be narrowed down",
                "score": 6
            },
            {
                "text": "Ignore the update for now and revisit it only if users begin reporting visible issues",
                "score": 0
            },
            {
                "text": "Wipe the system and rebuild it immediately so the update path starts from a clean image",
                "score": 1
            }
        ],
        "feedback": "Checking the failure details is the strongest next step because it explains why the update did not apply. Ignoring failed updates can lead to stability or security problems. Rebuilding the system is a last resort, not an initial response.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_local_016",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A user can sign in with cached credentials while offline, but cannot authenticate to the domain when connected. What should you check first?",
        "choices": [
            {
                "text": "Check whether the workstation can reach and resolve the domain resources needed for authentication",
                "score": 7
            },
            {
                "text": "Replace the keyboard and confirm whether the new hardware changes the connected sign-in result",
                "score": 1
            },
            {
                "text": "Create a second account for the user and test whether a new identity reaches the domain correctly",
                "score": 2
            }
        ],
        "feedback": "Cached credentials explain why offline sign-in works, so the next step is to verify domain connectivity and resolution. Replacing the keyboard does not fit the symptom. Creating another user account avoids the real problem instead of diagnosing domain access.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_memory_017",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A system is slowing down and available memory is almost gone. What is the best first step?",
        "choices": [
            {
                "text": "Check which processes are consuming memory so you can tell whether usage is expected or abnormal",
                "score": 6
            },
            {
                "text": "Restart the PC immediately and see whether memory usage resets to a stable baseline afterward",
                "score": 3
            },
            {
                "text": "Replace the monitor so the user can continue working while the slowdown is reassessed later",
                "score": 0
            }
        ],
        "feedback": "Looking at memory-heavy processes is the best way to tell whether the issue is normal use, a leak, or a runaway app. Restarting may temporarily improve performance but removes useful context before you inspect it. Replacing unrelated hardware does not match the symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_dhcp_018",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 9},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A workstation has no usable IP address. What should you investigate first?",
        "choices": [
            {
                "text": "Check DHCP assignment and verify whether the adapter is receiving or failing to receive a valid lease",
                "score": 7
            },
            {
                "text": "Replace the workstation and test whether new hardware receives an address normally",
                "score": 0
            },
            {
                "text": "Map a network drive to see whether the machine can still reach shared resources indirectly",
                "score": 1
            }
        ],
        "feedback": "A missing or unusable IP address points directly to network configuration or DHCP behavior. Replacing the workstation is too drastic before checking lease assignment. Mapping a drive does not solve or meaningfully diagnose the lack of a valid address.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_keyboard_019",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 2}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A user says the keyboard is typing the wrong characters. What is the best first check?",
        "choices": [
            {
                "text": "Verify the keyboard language and layout settings to confirm the device is using the expected input map",
                "score": 5
            },
            {
                "text": "Reinstall the operating system so all keyboard settings return to a default state",
                "score": 0
            }
        ],
        "feedback": "Unexpected characters are often caused by the wrong layout or language selection. Reinstalling the operating system is much too disruptive for what is commonly a simple settings issue.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_display_020",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 2}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A second monitor is not being detected. What should you do first?",
        "choices": [
            {
                "text": "Check the display cable and monitor settings to confirm the second screen is physically and logically connected",
                "score": 5
            },
            {
                "text": "Replace the graphics card and see whether the new hardware recognizes both displays correctly",
                "score": 1
            }
        ],
        "feedback": "Connection and display settings are common reasons a second monitor is missing. Replacing the graphics card is too aggressive as an initial troubleshooting step.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_app_021",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "An application will not launch on a user's PC. What is the most useful first step?",
        "choices": [
            {
                "text": "Check for errors, logs, or a hung process so you can tell why the launch is failing",
                "score": 6
            },
            {
                "text": "Reinstall the full operating system and confirm whether the application launches in the rebuilt environment",
                "score": 0
            },
            {
                "text": "Delete the application folder immediately and rebuild the app from a fresh install afterward",
                "score": 1
            }
        ],
        "feedback": "The strongest first move is to gather the information the application is already giving you through errors or process state. Reinstalling the operating system is far too broad. Deleting the application folder immediately is destructive and removes useful context before diagnosis.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_logon_022",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 8},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 7,
        "question": "A user says logging into Windows takes much longer than usual. What should you check first?",
        "choices": [
            {
                "text": "Check startup items, mapped resources, and any network-dependent actions that run during sign-in",
                "score": 7
            },
            {
                "text": "Replace the PC so the user can try the same login workflow on fresh hardware",
                "score": 1
            },
            {
                "text": "Explain that long login times can happen and advise the user to keep waiting each morning",
                "score": 0
            }
        ],
        "feedback": "Slow logons are often caused by startup apps, scripts, mapped drives, or network waits during sign-in. Replacing the PC is not justified by the symptom alone. Simply telling the user to wait avoids actual troubleshooting.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_cache_023",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 2}
        },
        "location": "helpdesk",
        "points": 6,
        "question": "A user sees old content on a webpage while others see the updated version. What should you try first?",
        "choices": [
            {
                "text": "Clear browser cache or force-refresh the page so the browser requests fresh content from the site",
                "score": 6
            },
            {
                "text": "Restart the web server and check whether the user's browser begins showing the newer version afterward",
                "score": 2
            }
        ],
        "feedback": "If only one user sees stale content, local caching is the strongest first explanation. Restarting the web server is more disruptive and less justified for a single-user symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_link_024",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 7},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 2}
        },
        "location": "helpdesk",
        "points": 5,
        "question": "A desktop cannot connect over Ethernet. What should you check first?",
        "choices": [
            {
                "text": "Check the cable seating and link lights on both the NIC and switch side of the connection",
                "score": 5
            },
            {
                "text": "Replace the network switch and retest the same workstation on the rebuilt connection path",
                "score": 1
            }
        ],
        "feedback": "Physical connectivity is the simplest and most relevant first check for an Ethernet failure. Replacing the entire switch is much too broad as an initial response.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "easy_access_025",
        "question_difficulty": "easy",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 9},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 3}
        },
        "location": "helpdesk",
        "points": 8,
        "question": "A user changed roles recently and now says they are missing access they should have. What should you check first?",
        "choices": [
            {
                "text": "Check the user's current group memberships and compare them to the access expected for the new role",
                "score": 8
            },
            {
                "text": "Grant the requested access manually so the user can work while the new role settles into place",
                "score": 4
            },
            {
                "text": "Tell the user to wait a few days before anyone checks the access model or role mapping",
                "score": 1
            }
        ],
        "feedback": "Role-based access is usually controlled through group membership, so that is the strongest first place to look. Granting manual access may solve the immediate symptom but can bypass the intended permission model. Waiting without checking anything is weak support practice.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_dns_001",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 3},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 20,
        "question": "Users can reach internal servers by IP, but several internal hostnames fail intermittently. What should you check first?",
        "choices": [
            {
                "text": "Review internal DNS records, client DNS settings, and whether stale entries or old cache data are involved",
                "score": 20
            },
            {
                "text": "Flush DNS on the affected machines and test whether the issue follows specific systems or specific names",
                "score": 15
            },
            {
                "text": "Restart the impacted servers to refresh services that may not have registered correctly",
                "score": 7
            }
        ],
        "feedback": "The strongest first step is to verify whether the DNS data itself is wrong, stale, or being queried incorrectly. Flushing client DNS is a reasonable troubleshooting step and may help isolate whether the problem is local caching, but it does not confirm whether the DNS records are actually correct. Restarting servers can sometimes refresh registrations, but it is a broader action that skips verification.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_gpo_002",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 3},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 24,
        "question": "A new Group Policy setting is applying to some users but not others in the same department. What is the best next step?",
        "choices": [
            {
                "text": "Check OU placement, inheritance, and security filtering to confirm the affected users are actually in scope",
                "score": 24
            },
            {
                "text": "Run gpupdate /force and compare gpresult output between a working user and a failing user",
                "score": 18
            },
            {
                "text": "Restart the domain controller that processed the most recent policy change to clear any stale state",
                "score": 8
            }
        ],
        "feedback": "The most reliable answer checks whether the policy is targeted correctly in the first place. Comparing gpresult and forcing updates is a strong troubleshooting step and useful for validation, but it usually comes after or alongside checking scope. Restarting a domain controller is not tightly matched to a scoping issue and is more disruptive.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_vpn_003",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 3},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 22,
        "question": "A remote user can connect to VPN, but cannot access internal resources once connected. What should you investigate first?",
        "choices": [
            {
                "text": "Check route assignment, internal DNS resolution, and whether the VPN session received the expected network settings",
                "score": 22
            },
            {
                "text": "Reinstall the VPN client and verify whether the same issue happens after a clean reconnect",
                "score": 13
            },
            {
                "text": "Reset the user's password and force a new VPN login session with fresh credentials",
                "score": 6
            }
        ],
        "feedback": "If VPN connects successfully but internal access fails, the strongest lead is routing, DNS, or tunnel configuration. Reinstalling the client is not unreasonable and may help if the configuration is corrupted, but it is less targeted than checking what settings the tunnel is actually providing. Resetting the password is weak because authentication already worked.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_mail_004",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 21,
        "question": "Several users report Outlook repeatedly asking for credentials, but they can still sign into other services. What should you check first?",
        "choices": [
            {
                "text": "Review cached credentials, authentication prompts, and whether the mail profile is pointing to the expected service endpoint",
                "score": 21
            },
            {
                "text": "Create a new Outlook profile for one affected user and compare behavior against the current profile",
                "score": 16
            },
            {
                "text": "Reset passwords for the affected users and monitor whether the prompts stop during the next login cycle",
                "score": 8
            }
        ],
        "feedback": "Checking cached credentials and endpoint/profile alignment best matches the symptom because other services still authenticate. Building a fresh profile is a solid diagnostic move and may fix the issue, but it is somewhat heavier than first checking credential and endpoint state. Password resets can help in limited cases but are less convincing when the issue is service-specific.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_share_005",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 3},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 23,
        "question": "A shared folder is accessible to some users but returns access denied for others who should have the same access. What is the best next step?",
        "choices": [
            {
                "text": "Compare share permissions, NTFS permissions, and group membership between a working user and a failing user",
                "score": 23
            },
            {
                "text": "Grant temporary direct access to an affected user and use that test to narrow down whether the issue is permission-related",
                "score": 15
            },
            {
                "text": "Restart the file server and verify whether the access denied behavior persists after services reload",
                "score": 6
            }
        ],
        "feedback": "Comparing a working user and a failing user gives the cleanest path to the underlying permission difference. Granting temporary direct access can help isolate whether permissions are the root cause, but it is more of a workaround and can muddy the access model. Restarting the server is a weaker fit because the problem already looks like authorization, not availability.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_dhcp_006",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 25,
        "question": "Newly connected devices are intermittently failing to receive valid IP addresses. What should you check first?",
        "choices": [
            {
                "text": "Review DHCP scope utilization, lease availability, and whether the DHCP service is handing out addresses correctly",
                "score": 25
            },
            {
                "text": "Assign temporary static IP addresses to a few affected devices to see whether the issue is limited to lease assignment",
                "score": 17
            },
            {
                "text": "Restart the affected workstations and test whether new leases are issued after a clean boot",
                "score": 8
            }
        ],
        "feedback": "Checking DHCP scope health is the best first step because it directly tests whether address assignment is the actual failure. Temporary static IPs can be a useful diagnostic move for isolating DHCP from general connectivity, but they do not explain why leasing is failing. Restarting clients may occasionally help but is less targeted than examining the lease source.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_web_007",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 18,
        "question": "An internal web application loads fine on Wi-Fi but fails when the same laptop is docked on Ethernet. What should you compare first?",
        "choices": [
            {
                "text": "Compare IP configuration, DNS, gateway, and VLAN behavior between the Wi-Fi and Ethernet connections",
                "score": 18
            },
            {
                "text": "Swap the docking adapter and verify whether the failure follows the hardware path or the network path",
                "score": 13
            },
            {
                "text": "Reinstall the application client and test whether the protocol stack re-registers correctly after reinstall",
                "score": 6
            }
        ],
        "feedback": "Because the same machine behaves differently based on connection type, the strongest first move is to compare the two network paths directly. Swapping the dock or adapter is a fair diagnostic test and can rule out local hardware, but it still comes after checking whether the network settings themselves differ. Reinstalling the application is less tied to the symptom.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_profile_008",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 19,
        "question": "A user signs into a domain PC and gets a temporary profile instead of their normal desktop. What is the best first step?",
        "choices": [
            {
                "text": "Check event logs, profile path access, and whether the expected profile is loading or failing during sign-in",
                "score": 19
            },
            {
                "text": "Rename the local profile folder and test whether Windows can build a clean profile path on next login",
                "score": 14
            },
            {
                "text": "Recreate the entire user account and migrate the user's data into a new identity",
                "score": 5
            }
        ],
        "feedback": "The best first move is to verify why the profile is failing rather than immediately changing data or identity state. Renaming the profile folder can be a workable fix if corruption is local, but it is more intrusive than checking logs and path access first. Recreating the user account is too broad for a profile loading issue.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_cert_009",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 20,
        "question": "Some users are getting certificate warnings on an internal site, while others are not. What should you check first?",
        "choices": [
            {
                "text": "Compare trust stores, intermediate certificates, and trust-chain behavior between working and failing clients",
                "score": 20
            },
            {
                "text": "Rebind the current certificate on the web server and test whether client warnings stop after the service refreshes",
                "score": 14
            },
            {
                "text": "Instruct users to continue through the warning while you confirm whether it is only cosmetic",
                "score": 2
            }
        ],
        "feedback": "Because only some users are affected, client trust differences and chain validation are the strongest lead. Rebinding the certificate is not unreasonable and may help if the service is presenting the wrong chain, but it is broader than first comparing client trust behavior. Telling users to bypass warnings is unsafe and treats the problem as harmless without verification.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_script_010",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 3},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": False, "weight": 0}
        },
        "location": "helpdesk",
        "points": 22,
        "question": "A login script that maps department drives is not running for several users after a recent OU change. What is the best first step?",
        "choices": [
            {
                "text": "Check GPO links, script path access, and whether the OU move changed inheritance or targeting",
                "score": 22
            },
            {
                "text": "Run the script manually for one affected user and compare the result with a user who still gets it automatically",
                "score": 16
            },
            {
                "text": "Recreate the drive mappings as permanent manual mappings for the affected department",
                "score": 8
            }
        ],
        "feedback": "Since the issue appeared after an OU move, policy scope and inheritance are the strongest first checks. Running the script manually is a useful validation step and can separate script failure from policy delivery failure, but it does not answer why the targeting changed. Manual permanent mappings restore function but sidestep the root cause.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_trust_011",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 28,
        "question": "A workstation suddenly shows a trust relationship error when a domain user tries to sign in. What is the best next step?",
        "choices": [
            {
                "text": "Repair the workstation trust with the domain or rejoin the machine after confirming the trust issue",
                "score": 28
            },
            {
                "text": "Test domain reachability and secure channel behavior from the workstation before changing the machine account state",
                "score": 21
            },
            {
                "text": "Reset the user's password and retry sign-in using a fresh credential token",
                "score": 7
            }
        ],
        "feedback": "Repairing the machine trust is the best corrective step when the trust relationship is actually broken. Testing secure channel behavior and connectivity first is also a strong answer because it confirms the diagnosis before making changes, but it is slightly less direct as an immediate next step. Resetting the user's password does not fit a machine trust failure.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_service_012",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 24,
        "question": "A Windows service starts successfully, then stops after a few seconds. What should you check first?",
        "choices": [
            {
                "text": "Check dependency services, startup parameters, and event log entries tied to the service shutdown",
                "score": 24
            },
            {
                "text": "Change the service account and retry the startup to test whether the failure is tied to credentials",
                "score": 16
            },
            {
                "text": "Restart the server so the service has a clean startup environment and test whether it holds",
                "score": 9
            }
        ],
        "feedback": "Looking at dependencies and logs is the strongest first move because the service is starting and then immediately failing for a reason that should be visible. Changing the service account can be a good targeted diagnostic if identity is suspected, but it is still a change before diagnosis. Restarting the server may help in edge cases but is broader and less informative.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_spooler_013",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 23,
        "question": "A printer deployed by policy appears on user machines, but jobs remain stuck in queue and never print. What should you check first?",
        "choices": [
            {
                "text": "Check spooler health, printer queue status, and driver compatibility on the print path",
                "score": 23
            },
            {
                "text": "Remove and redeploy the printer to one affected machine to test whether the deployment artifact is corrupted",
                "score": 15
            },
            {
                "text": "Change the printer to a generic driver immediately and see whether jobs begin moving afterward",
                "score": 11
            }
        ],
        "feedback": "The strongest answer checks the actual queue, spooler, and driver interaction first because the printer is already present but failing to process jobs. Redeploying to one machine is a fair test and may isolate whether the deployment object is bad, but it is not as direct as checking the queue path. Swapping to a generic driver might work, yet it changes configuration before confirming the real cause.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_delays_014",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 26,
        "question": "Email delivery is delayed for many users across the organization, but messages eventually arrive. What should you investigate first?",
        "choices": [
            {
                "text": "Review the transport queue, delivery retry behavior, and any service or connector health alerts",
                "score": 26
            },
            {
                "text": "Send controlled test messages between internal and external recipients to narrow down where the delay appears",
                "score": 19
            },
            {
                "text": "Restart mail clients on affected user machines and compare whether new messages leave the Outbox faster",
                "score": 6
            }
        ],
        "feedback": "Checking transport and queue health is the strongest first step because the symptom is organization-wide and server-side behavior is most likely. Running controlled message tests is also a good diagnostic approach and helps isolate where delay occurs, but it comes slightly after checking the queueing system directly. Restarting clients is weak for a broad delivery delay.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_perf_015",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 21,
        "question": "An internal application became slow for everyone immediately after a version update. What is the best first step?",
        "choices": [
            {
                "text": "Review the change introduced by the update and compare current logs or configuration with the pre-update state",
                "score": 21
            },
            {
                "text": "Roll one server back to the previous version in a controlled test and compare performance behavior",
                "score": 17
            },
            {
                "text": "Increase server resources and monitor whether the slowdown is reduced under the new version",
                "score": 10
            }
        ],
        "feedback": "Checking the update and comparing logs/config is the strongest starting point because the timing directly implicates the change. A controlled rollback test is also a strong option and can validate whether the update caused the slowdown, but it is a more active change. Increasing resources may help performance, yet it assumes capacity is the problem rather than the update itself.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_ports_016",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 22,
        "question": "A service shows as running on the server, but clients cannot connect to it. What should you check first?",
        "choices": [
            {
                "text": "Verify the expected listening ports, network reachability, and any firewall rules between clients and the service",
                "score": 22
            },
            {
                "text": "Restart the service and confirm whether it binds to the correct interface after a clean start",
                "score": 15
            },
            {
                "text": "Reinstall the client on one affected machine to see whether the problem is application-side only",
                "score": 7
            }
        ],
        "feedback": "If a service is running but unreachable, the strongest lead is whether it is truly listening and reachable across the network path. Restarting the service is a fair secondary step and may help if binding failed, but it is less informative than checking the port state directly. Reinstalling a client is weaker because the symptom may exist before the client even reaches the service.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_dns_017",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 27,
        "question": "Internal users are being sent to the wrong internal site when using a hostname that should point elsewhere. What should you check first?",
        "choices": [
            {
                "text": "Check internal DNS data, stale records, and cached resolution on both clients and relevant servers",
                "score": 27
            },
            {
                "text": "Test the hostname from multiple subnets and compare whether the incorrect destination appears consistently or only in certain places",
                "score": 21
            },
            {
                "text": "Restart the site that should be receiving traffic so it can re-register itself in the environment",
                "score": 9
            }
        ],
        "feedback": "Checking the actual DNS data and cache state is the strongest first move because the hostname is resolving to the wrong destination. Testing from multiple subnets is also a strong diagnostic action and helps isolate scope, but it usually follows or complements direct DNS inspection. Restarting the application site is weaker because the symptom is name resolution, not availability alone.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_disk_018",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 24,
        "question": "A file server suddenly reports critically low disk space overnight. What is the best first step?",
        "choices": [
            {
                "text": "Review recent growth, large file creation, logs, and scheduled jobs before deleting or expanding anything",
                "score": 24
            },
            {
                "text": "Expand the volume temporarily and use the added space to gather data without immediate user impact",
                "score": 17
            },
            {
                "text": "Delete the newest large files to restore service quickly and investigate later",
                "score": 8
            }
        ],
        "feedback": "The strongest answer investigates why space disappeared before changing or removing data. Expanding the volume can be a reasonable stabilization step if the situation is critical, but it still avoids the cause and may delay root-cause analysis. Deleting files immediately can destroy useful data or evidence and is riskier.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_ad_019",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 26,
        "question": "A user's group membership was changed on one domain controller, but another system still does not reflect the change hours later. What should you check first?",
        "choices": [
            {
                "text": "Check replication status and whether the relevant domain controllers are exchanging changes normally",
                "score": 26
            },
            {
                "text": "Sign the user out and back in to force a fresh token and test whether the issue is token-related rather than replication-related",
                "score": 17
            },
            {
                "text": "Recreate the user account and reapply the desired group memberships from scratch",
                "score": 5
            }
        ],
        "feedback": "If one domain controller has the change and another appears not to, replication is the strongest first thing to examine. Refreshing the user's token is a reasonable diagnostic move if the directory change has already replicated and the symptom is authorization, but the prompt suggests the directory state itself is inconsistent. Recreating the user is excessive.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_vlan_020",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 23,
        "question": "A user moved desks and can reach the internet, but cannot access internal systems they used before. What is the best first check?",
        "choices": [
            {
                "text": "Check whether the new switch port and subnet placement put the device on the expected VLAN and internal route path",
                "score": 23
            },
            {
                "text": "Compare the moved user's IP details to a nearby workstation that still has normal internal access",
                "score": 18
            },
            {
                "text": "Reinstall the user's machine on the assumption that the move corrupted the network profile",
                "score": 4
            }
        ],
        "feedback": "Because the issue began after a desk move, checking VLAN or switch-port placement is the strongest answer. Comparing the moved workstation's network details to a working one is also a very good diagnostic step and closely related, but it is slightly less direct than checking the port configuration itself. Reinstalling the machine is poorly matched to the timing.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_roaming_021",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 20,
        "question": "A user's desktop settings and documents are not following them between domain PCs as expected. What should you check first?",
        "choices": [
            {
                "text": "Check whether roaming profile or folder redirection settings are applying and whether the profile path is reachable",
                "score": 20
            },
            {
                "text": "Compare one working user and one failing user to confirm whether the issue is tied to policy application or path access",
                "score": 16
            },
            {
                "text": "Copy the user's data manually between systems until the normal profile behavior resumes",
                "score": 8
            }
        ],
        "feedback": "Checking the profile or folder redirection configuration is the best first move because it addresses the mechanism intended to carry settings and documents. Comparing a working user to a failing user is also a strong diagnostic approach, but it usually supports the same underlying check rather than replacing it. Manual copying is only a workaround.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_proxy_022",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 22,
        "question": "Several users can browse some websites but fail on others after a recent network configuration change. What should you investigate first?",
        "choices": [
            {
                "text": "Review proxy settings, filtering rules, and the exact change that altered outbound web handling",
                "score": 22
            },
            {
                "text": "Run controlled tests from more than one client to compare which destinations fail and whether the issue follows user, site, or path",
                "score": 17
            },
            {
                "text": "Reinstall the browsers used by the affected users to eliminate client-side corruption as a factor",
                "score": 6
            }
        ],
        "feedback": "The strongest answer focuses on the recent network change and the policy layer that now treats destinations differently. Controlled client tests are also useful and can help isolate scope, but they come just after examining the configuration change itself. Reinstalling browsers is less convincing when multiple users are affected after a network change.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_backup_023",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 9},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 25,
        "question": "Backups have been completing successfully for weeks, but restore tests are failing. What is the best next step?",
        "choices": [
            {
                "text": "Review backup job logs, restore settings, and whether the backups are complete and usable rather than only marked successful",
                "score": 25
            },
            {
                "text": "Run a limited restore to a test location using the most recent successful set and compare the failure details against earlier sets",
                "score": 19
            },
            {
                "text": "Run the backups again on the next cycle before looking deeper into restore behavior",
                "score": 8
            }
        ],
        "feedback": "The best answer checks whether the backup chain and restore configuration are actually valid. Running a controlled restore test is also a strong option and helps narrow the failure, but it is slightly more active than first reading the job and restore details already available. Re-running backups without diagnosing restore failure avoids the core issue.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_sched_024",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 8},
            "hard": {"allowed": True, "weight": 5}
        },
        "location": "helpdesk",
        "points": 21,
        "question": "A task that should run nightly on a server has stopped running, but the script still works when launched manually. What should you check first?",
        "choices": [
            {
                "text": "Check Task Scheduler triggers, execution history, and the credentials or permissions used by the scheduled context",
                "score": 21
            },
            {
                "text": "Create a duplicate scheduled task under a different account and compare whether it executes successfully overnight",
                "score": 16
            },
            {
                "text": "Run the task manually each morning until the schedule starts working again",
                "score": 7
            }
        ],
        "feedback": "Because the script works manually, the scheduler context is the strongest first area to inspect. Creating a duplicate task under another account is a valid diagnostic test, but it is a change rather than an initial inspection. Running the task manually is only a workaround and does not explain why the schedule broke.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "medium_auth_025",
        "question_difficulty": "medium",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 10},
            "hard": {"allowed": True, "weight": 6}
        },
        "location": "helpdesk",
        "points": 27,
        "question": "Users can authenticate to some internal services but fail on others after a recent DNS change. What should you investigate first?",
        "choices": [
            {
                "text": "Check whether the affected services now resolve to the correct systems and whether service-related DNS records still match expectations",
                "score": 27
            },
            {
                "text": "Compare a working service and a failing service from the same client to see whether the failure follows hostname, endpoint, or service type",
                "score": 21
            },
            {
                "text": "Reset passwords for the affected users and clear all saved credentials before testing again",
                "score": 7
            }
        ],
        "feedback": "Because the failures began after a DNS change and only affect some services, checking how those services resolve is the strongest answer. Comparing a working and failing service from the same client is also a strong troubleshooting move and can help isolate whether the issue is resolution or service-specific, but it still follows the same underlying hypothesis. Password resets are a weaker fit.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_auth_001",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 42,
        "question": "Several users intermittently fail domain authentication. Logs show Kerberos errors, but password resets do not help. What should you check first?",
        "choices": [
            {
                "text": "Review time synchronization and DNS pathing for affected clients and domain controllers involved in the failures",
                "score": 42
            },
            {
                "text": "Capture one failed sign-in path and compare it to a successful sign-in path to identify whether the issue follows a specific DC or client group",
                "score": 34
            },
            {
                "text": "Restart the affected clients and domain controllers in a controlled order to clear stale authentication state",
                "score": 16
            },
            {
                "text": "Reset the passwords again and require all affected users to sign in with fresh credentials",
                "score": 7
            }
        ],
        "feedback": "Checking time sync and DNS is the strongest first move because Kerberos depends directly on both. Comparing failed and successful sign-ins is also a very strong diagnostic step and helps narrow scope, but it is slightly less direct than first validating the core Kerberos dependencies already suggested by the logs. Restarting systems may help with stale state but does not explain the cause. Additional password resets are weak because that angle has already been tested.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_net_002",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 1},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 45,
        "question": "Multiple users report intermittent connectivity loss. Network logs show repeated ARP conflicts. What is the best first response?",
        "choices": [
            {
                "text": "Trace the conflicting ARP entries to identify the duplicate IP assignment and correct the addressing issue",
                "score": 45
            },
            {
                "text": "Isolate one impacted segment and compare switch tables or client lease data to determine whether the conflict is DHCP-driven or static",
                "score": 36
            },
            {
                "text": "Restart the affected switches to clear learned state and see whether the conflict pattern resets",
                "score": 15
            },
            {
                "text": "Assign new static IPs to the impacted users so they can reconnect while the rest of the network settles",
                "score": 11
            }
        ],
        "feedback": "The strongest answer directly identifies the duplicate addressing source causing the ARP conflict. Segment-level isolation and comparison of leases versus static assignments is also very strong and useful for narrowing the cause, but it is slightly less direct than resolving the conflicting entries themselves. Restarting switches may hide the issue temporarily without fixing it. Assigning more static IPs can make address management worse.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_ad_003",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 1},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 44,
        "question": "Changes made on one domain controller are not appearing on another site hours later. What should you investigate first?",
        "choices": [
            {
                "text": "Review replication health, site-link behavior, and the connectivity path between the affected domain controllers",
                "score": 44
            },
            {
                "text": "Compare directory metadata on both controllers to confirm whether the delay is replication, lingering objects, or stale reads",
                "score": 35
            },
            {
                "text": "Restart both domain controllers so replication services reinitialize and retry the pending changes",
                "score": 16
            },
            {
                "text": "Recreate the missing changes manually on the second site to restore consistency more quickly",
                "score": 12
            }
        ],
        "feedback": "Checking replication health and inter-site behavior is the strongest first move because the problem is cross-site inconsistency. Comparing metadata is also a strong investigative option and can help distinguish several replication failure modes, but it follows the same diagnosis path rather than replacing the initial health check. Restarting controllers is broader and less precise. Manual recreation risks masking the actual replication issue.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_dns_004",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 41,
        "question": "Internal users are intermittently sent to the wrong internal server by hostname. What should you check first?",
        "choices": [
            {
                "text": "Review the DNS records, cache state, and stale registration behavior tied to the hostname in question",
                "score": 41
            },
            {
                "text": "Query the hostname from multiple client groups and compare whether the wrong destination follows subnet, resolver, or client cache",
                "score": 33
            },
            {
                "text": "Restart the intended application server and force it to reregister its network identity",
                "score": 13
            },
            {
                "text": "Hardcode the expected IP on the affected clients until normal resolution behavior returns",
                "score": 10
            }
        ],
        "feedback": "Checking the DNS data and cache state is the strongest first step because the hostname is resolving incorrectly. Multi-client testing is also a strong diagnostic method and helps isolate scope, but it is slightly less direct than checking the resolution source itself. Restarting the target server may help if registration failed, but it is still a broader action. Hardcoding clients is a workaround that creates future maintenance problems.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_security_005",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 1},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 50,
        "question": "Multiple user accounts show failed sign-in attempts from unfamiliar external IP addresses within a short time window. What is the best first action?",
        "choices": [
            {
                "text": "Contain the affected accounts and escalate as a likely security incident while preserving the relevant authentication evidence",
                "score": 50
            },
            {
                "text": "Correlate the failed sign-ins across accounts and services first so you can confirm whether the pattern is password spray before containment",
                "score": 38
            },
            {
                "text": "Reset the affected passwords immediately and continue monitoring whether the attempts persist afterward",
                "score": 24
            },
            {
                "text": "Wait to see whether the activity escalates into successful logins before involving security responders",
                "score": 5
            }
        ],
        "feedback": "Containment and escalation are strongest because the pattern already suggests an active threat. Correlation work is useful and can sharpen the incident picture, but it should not delay a reasonable containment response. Password resets may help reduce immediate exposure but do not address the broader event on their own. Waiting for successful compromise is too passive.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_backup_006",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 43,
        "question": "Backup jobs have been reporting success, but test restores consistently fail. What should you do first?",
        "choices": [
            {
                "text": "Review backup logs, restore settings, and chain integrity to determine why valid backups are not producing valid restores",
                "score": 43
            },
            {
                "text": "Perform a controlled restore from more than one backup point to determine whether the failure is tied to a specific generation or the restore workflow itself",
                "score": 35
            },
            {
                "text": "Run another backup cycle before testing restores again so the newest set is definitely fresh",
                "score": 11
            },
            {
                "text": "Delete the existing backup set and rebuild the schedule from scratch to eliminate any legacy issues",
                "score": 8
            }
        ],
        "feedback": "The strongest answer examines why restore functionality is broken even though backups show success. Controlled restores across more than one generation are also a strong diagnostic move and help isolate whether the problem is data-set specific or workflow-specific, but they follow closely after checking the restore and backup details already available. Re-running backups does not fix restore failure. Deleting backups too early risks losing usable recovery points.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_vpn_007",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 1},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 46,
        "question": "VPN users are receiving IPs from an unexpected network range and cannot reach protected internal systems. What should you check first?",
        "choices": [
            {
                "text": "Review the VPN address pool, route assignment, and any access rules tied to the issued range",
                "score": 46
            },
            {
                "text": "Capture a working and failing VPN session to compare assigned routes, DNS, and policy attributes side by side",
                "score": 37
            },
            {
                "text": "Restart the VPN service and compare whether the next sessions return to the expected address pool",
                "score": 15
            },
            {
                "text": "Assign manual static addresses to the remote users who need immediate access",
                "score": 8
            }
        ],
        "feedback": "Checking the VPN pool and policy logic is the best first move because the wrong addresses are being assigned at the source. Comparing a working and failing session is also a strong diagnostic method and helps isolate which session attributes differ, but it is slightly less direct than inspecting the server-side policy first. Restarting the service may temporarily change behavior without explaining it. Manual addressing is a workaround.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_storage_008",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 42,
        "question": "A file server loses a large amount of disk space overnight, and users also report unusual file renames. What is the best first response?",
        "choices": [
            {
                "text": "Investigate the file activity immediately and escalate the event as a possible active incident before normal cleanup actions",
                "score": 42
            },
            {
                "text": "Place the share in a limited-access state and collect recent file-change details so you can determine whether automation or malware is responsible",
                "score": 36
            },
            {
                "text": "Expand the volume temporarily so service remains available while you review the changed data afterward",
                "score": 18
            },
            {
                "text": "Delete the newest large files first so the volume returns to normal and then revisit the renames later",
                "score": 7
            }
        ],
        "feedback": "The strongest first response is to treat the combination of sudden space loss and unusual renames as potentially malicious and investigate immediately. Restricting access and collecting change data is also a strong containment-oriented response, but it is slightly more tactical than the broader incident-first framing. Expanding storage may keep service alive but does not address the apparent abnormal activity. Deleting files can remove evidence or worsen impact.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_gpo_009",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 2},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 40,
        "question": "After a new Group Policy deployment, many machines become noticeably slower during login and startup. What should you investigate first?",
        "choices": [
            {
                "text": "Review the newly deployed policy settings and identify which recent change aligns with the slowdown pattern",
                "score": 40
            },
            {
                "text": "Compare one affected machine and one unaffected machine with policy-result data to isolate which setting is adding delay",
                "score": 33
            },
            {
                "text": "Restart the impacted machines and see whether the next boot applies the policy more cleanly",
                "score": 13
            },
            {
                "text": "Disable unrelated background software globally to reduce boot-time overhead while the issue is present",
                "score": 7
            }
        ],
        "feedback": "Reviewing the changed policy itself is the strongest first step because the slowdown appeared directly after deployment. Comparing affected and unaffected machines is also strong and can isolate the exact setting, but it follows naturally after acknowledging that the recent policy change is the likely source. Restarting repeats the same condition without diagnosis. Disabling unrelated software is too speculative.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_service_010",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": True, "weight": 1},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 41,
        "question": "An internal application service shows as running, but clients cannot connect and port tests fail. What is the best first step?",
        "choices": [
            {
                "text": "Verify whether the service is truly listening on the expected interface and whether firewalls allow the connection path",
                "score": 41
            },
            {
                "text": "Compare local service port state to a known-good server running the same application stack",
                "score": 34
            },
            {
                "text": "Restart the service and check whether the port binds properly after a clean startup cycle",
                "score": 14
            },
            {
                "text": "Reinstall the clients that are reporting connection failures to eliminate workstation-side variables",
                "score": 6
            }
        ],
        "feedback": "Confirming whether the service is actually listening and reachable is the strongest first step because the failure appears before the application layer fully engages. Comparing against a known-good server is also a strong diagnostic method, but it is slightly less direct than checking the affected service's port and firewall state. Restarting the service may help if binding failed, but it is still a change before diagnosis. Reinstalling clients is weaker.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_proxy_011",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 43,
        "question": "After a firewall policy change, users can reach some external sites but fail on others in inconsistent ways. What should you check first?",
        "choices": [
            {
                "text": "Review the changed firewall, proxy, or filtering logic and map the failures to the new outbound policy behavior",
                "score": 43
            },
            {
                "text": "Run controlled browsing tests from multiple users and compare the failing destinations against category, protocol, or path differences",
                "score": 35
            },
            {
                "text": "Clear browser caches and authentication tokens on the most heavily impacted user machines",
                "score": 9
            },
            {
                "text": "Roll back the browser version on the affected workstations to rule out client rendering regressions",
                "score": 7
            }
        ],
        "feedback": "The strongest first move is to connect the symptom pattern to the known firewall change. Controlled browsing tests are also strong and help isolate scope and traffic class, but they complement rather than replace checking the changed policy. Cache clearing and browser rollback are weaker because the issue spans users after a network-layer change.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_identity_012",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 47,
        "question": "A machine reports a trust relationship failure, and other symptoms suggest the computer account password may be out of sync with the domain. What is the best response?",
        "choices": [
            {
                "text": "Repair the machine account trust or reset the secure channel after confirming the trust path is broken",
                "score": 47
            },
            {
                "text": "Validate secure channel status and domain reachability first, then decide whether the machine account needs repair",
                "score": 39
            },
            {
                "text": "Create a fresh user profile so the user can sign in under a newly built desktop context",
                "score": 8
            },
            {
                "text": "Shift the user to a permanent local account so work can continue without domain dependency",
                "score": 5
            }
        ],
        "feedback": "Repairing the machine trust is the strongest corrective action when the machine account relationship is the real failure. Validating the secure channel first is also a very strong answer because it confirms the diagnosis before altering the relationship, but it is slightly less direct as the response. Creating a new user profile does not fix machine trust. Permanent local-account use avoids the problem rather than solving it.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_dns_013",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 44,
        "question": "Internal domains resolve correctly, but external domains fail from the DNS servers themselves. What should you check first?",
        "choices": [
            {
                "text": "Review DNS forwarders, root hints, and whether the servers have working outbound DNS reachability",
                "score": 44
            },
            {
                "text": "Query several external names directly from the DNS servers and compare responses by forwarder path to isolate where resolution stops",
                "score": 35
            },
            {
                "text": "Point clients to public DNS temporarily so internet name resolution can continue while you investigate",
                "score": 15
            },
            {
                "text": "Restart the DNS service and wait for it to rebuild normal external resolution behavior",
                "score": 12
            }
        ],
        "feedback": "Checking forwarders, root hints, and outbound reachability is the strongest first step because internal resolution still works, which narrows the failure to external lookup handling. Direct query testing from the servers is also strong and helps isolate the break point, but it follows the same root hypothesis. Pointing clients elsewhere may restore some access temporarily, yet it bypasses the issue and can break internal resolution design. Restarting DNS is broader and less informative.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_forensics_014",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 49,
        "question": "A workstation shows an unknown process and unusual outbound traffic spikes to destinations users do not recognize. What is the best first action?",
        "choices": [
            {
                "text": "Isolate the workstation from the network and escalate while preserving as much investigative context as possible",
                "score": 49
            },
            {
                "text": "Capture the current connection and process details immediately before deciding whether to isolate the system",
                "score": 37
            },
            {
                "text": "Kill the suspicious process and monitor whether the traffic pattern stops without disconnecting the machine",
                "score": 20
            },
            {
                "text": "Restart the system and return it to the user if the traffic does not reappear right away",
                "score": 8
            }
        ],
        "feedback": "Isolation with escalation is strongest because suspicious outbound behavior can indicate compromise and active harm to the environment. Capturing connection and process details first is also a strong option if done quickly and safely, but it introduces some delay before containment. Killing the process may reduce symptoms while destroying useful evidence. Restarting can also erase context and is weaker.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_cert_015",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 42,
        "question": "An internal application suddenly begins showing certificate warnings across many systems after a certificate renewal. What should you check first?",
        "choices": [
            {
                "text": "Review the renewed certificate's binding, hostname match, and full trust chain as presented by the application",
                "score": 42
            },
            {
                "text": "Compare the old and new certificates to determine whether EKU, SAN, issuer chain, or binding behavior changed unexpectedly",
                "score": 34
            },
            {
                "text": "Restart the application service so the new certificate presentation path is fully refreshed",
                "score": 14
            },
            {
                "text": "Advise users to bypass the warning until the certificate environment stabilizes after renewal",
                "score": 2
            }
        ],
        "feedback": "The strongest first step is to verify what certificate is actually being presented and whether it matches trust and hostname expectations. Comparing old and new certificates is also a very strong diagnostic action, but it follows after confirming the current live presentation path. Restarting the service may help if the binding was not refreshed, but it is less precise than checking the certificate state directly. Bypassing warnings is unsafe.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_sched_016",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 40,
        "question": "An overnight scheduled task that updates shared data stops running after a service account password change. The script still works when launched manually by an admin. What should you check first?",
        "choices": [
            {
                "text": "Review the scheduled task credentials, execution context, and permission model tied to the service account change",
                "score": 40
            },
            {
                "text": "Clone the scheduled task under a separate account and compare whether the failure follows the task definition or the account context",
                "score": 31
            },
            {
                "text": "Restart the server and allow the task to retry under a clean system state on the next run",
                "score": 11
            },
            {
                "text": "Run the script manually each morning until the scheduled copy begins working again",
                "score": 9
            }
        ],
        "feedback": "Checking the stored credentials and execution context is the strongest answer because the failure began immediately after a service account password change. Cloning the task under another account is a strong diagnostic technique, but it is a change rather than a first inspection. Restarting the server does not directly address the credential mismatch. Manual daily execution is only a workaround.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_mail_017",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 41,
        "question": "Outbound mail is delayed for all users, and queue monitoring shows messages accumulating faster than they leave. What should you do first?",
        "choices": [
            {
                "text": "Review transport queue behavior, connector health, and the stage at which outbound delivery is backing up",
                "score": 41
            },
            {
                "text": "Send controlled internal-to-external tests and compare queue growth patterns by destination domain and message size",
                "score": 33
            },
            {
                "text": "Flush or clear selected queue items to see whether the transport backlog begins moving again",
                "score": 12
            },
            {
                "text": "Restart mail clients and have users resend delayed messages from scratch",
                "score": 5
            }
        ],
        "feedback": "The strongest answer examines the transport layer directly because queue growth shows the failure is server-side. Controlled test messages are also strong and help isolate where delivery breaks, but they come after or alongside checking the queue stage itself. Clearing queue items is risky and may destroy messages without fixing the cause. Restarting clients is a weak fit.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
            "id": "hard_replication_018",
            "question_difficulty": "hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": True, "weight": 9}
            },
            "location": "helpdesk",
            "points": 46,
            "question": "SYSVOL changes are visible on one domain controller but not another, and login scripts are inconsistent between sites. What should you check first?",
            "choices": [
                {
                    "text": "Review SYSVOL or DFS replication health and confirm the replication path between the relevant domain controllers",
                    "score": 46
                },
                {
                    "text": "Compare the script versions and timestamps on both controllers to determine whether the issue is truly replication or an update path mistake",
                    "score": 36
                },
                {
                    "text": "Copy the correct scripts manually to the missing controller so logins become consistent again while you continue checking",
                    "score": 15
                },
                {
                    "text": "Restart the affected client machines so they redraw the latest login resources from the domain",
                    "score": 6
                }
            ],
            "feedback": "Checking SYSVOL or DFS replication health is the strongest first step because the same domain content is inconsistent between controllers. Comparing file versions on both sides is also a strong diagnostic move and helps confirm whether replication is actually at fault, but it is slightly less direct than checking replication health itself. Manual copying can restore function but risks obscuring the root problem. Client restarts do not solve inconsistent SYSVOL content.",
            "allowed_days": [],
            "followup_event": {"allowed": False, "event_id": ""},
            "repeatable": False
    },

    {
        "id": "hard_latency_019",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 4},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 40,
        "question": "An application performs normally internally but becomes unusably slow for remote VPN users during peak hours only. What should you check first?",
        "choices": [
            {
                "text": "Review VPN throughput, latency, and peak-time path congestion between remote users and the application environment",
                "score": 40
            },
            {
                "text": "Compare application response timing from an internal host and a VPN-connected host during the same window to separate app delay from network delay",
                "score": 32
            },
            {
                "text": "Increase server-side application resources and monitor whether remote users improve during the next peak period",
                "score": 14
            },
            {
                "text": "Schedule a daily VPN service restart before peak hours so the tunnel environment begins from a clean state",
                "score": 9
            }
        ],
        "feedback": "Because only remote VPN users slow down and only during peak periods, the strongest first move is to inspect the VPN path and congestion profile. Internal versus VPN timing comparison is also a strong diagnostic step and helps prove whether the bottleneck is network or application, but it slightly follows the network-path hypothesis rather than replacing it. Increasing server resources may help if the application is borderline, but it does not fit the scope as well. Routine service restarts are a weak workaround.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_acl_020",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": True, "weight": 5},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 45,
        "question": "After a network redesign, one subnet can reach the internet but cannot access specific internal application ports used by a legacy service. What should you check first?",
        "choices": [
            {
                "text": "Review the ACLs, firewall rules, and route changes affecting the redesigned subnet's path to the legacy service",
                "score": 45
            },
            {
                "text": "Test the legacy ports from the affected subnet and a working subnet to identify whether the loss is policy-specific or route-specific",
                "score": 36
            },
            {
                "text": "Move the affected users to a temporary VLAN that still has the older access behavior while you observe traffic patterns",
                "score": 15
            },
            {
                "text": "Reinstall the client application used to reach the service on several failing systems",
                "score": 6
            }
        ],
        "feedback": "The strongest first step is to inspect the network policy and route changes introduced by the redesign. Comparing port access from working and failing subnets is also a strong diagnostic move and helps prove whether the failure is tied to policy or routing, but it follows the same root hypothesis. Moving users to another VLAN can restore function temporarily, though it avoids fixing the design. Reinstalling the client is weak because the symptom follows subnet placement.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_db_021",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 44,
        "question": "An application server can reach its database by IP, but the application still fails to authenticate after a recent service migration. What should you check first?",
        "choices": [
            {
                "text": "Review the connection string, service account permissions, and any name-based authentication dependencies introduced by the migration",
                "score": 44
            },
            {
                "text": "Compare the migrated server's application settings to the pre-migration environment to isolate which identity or endpoint detail changed",
                "score": 35
            },
            {
                "text": "Restart the database service and the application service together so the session and identity path reinitialize cleanly",
                "score": 12
            },
            {
                "text": "Replace hostname references with raw IP references everywhere in the application configuration and retest",
                "score": 10
            }
        ],
        "feedback": "If the server can reach the database by IP but authentication fails after migration, the strongest first step is to review how the application now identifies and authenticates to the database. Comparing migrated and pre-migration settings is also a strong method and helps surface exactly what changed, but it is slightly broader than checking the live connection and identity configuration first. Restarting services may clear state but does not diagnose the migration-related difference. Replacing hostnames with IPs may bypass some name-based issues but can break intended authentication behavior.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_eventlog_022",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 40,
        "question": "A critical service began failing after a system patch cycle, but only on one of several identically configured servers. What should you check first?",
        "choices": [
            {
                "text": "Compare logs, service state, and effective configuration between the failing server and a working peer",
                "score": 40
            },
            {
                "text": "Review the exact patch and application sequence on the failing host to determine whether one server diverged during the cycle",
                "score": 34
            },
            {
                "text": "Roll back the most recent patch from the failing server before collecting any additional diagnostics",
                "score": 16
            },
            {
                "text": "Restart the service several times across the patch window to see whether it stabilizes as dependencies settle",
                "score": 10
            }
        ],
        "feedback": "Comparing the failing server to a working peer is the strongest first move because the environment should be the same except for whatever diverged. Reviewing patch sequence on the failing host is also strong and may reveal the divergence, but it is slightly narrower than side-by-side comparison of overall state. Rolling back immediately can help if a patch is the cause, yet it changes the system before diagnosis. Repeated restarts are weaker.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_storage_023",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 9}
        },
        "location": "helpdesk",
        "points": 43,
        "question": "A shared storage volume is online, but only some application servers can write to it after a permission model change. What should you check first?",
        "choices": [
            {
                "text": "Review the volume ACLs, host access rules, and the service identities used by the servers that can and cannot write",
                "score": 43
            },
            {
                "text": "Compare a working application server and a failing one to determine whether the permission issue follows the host, service identity, or storage path",
                "score": 35
            },
            {
                "text": "Remove the write restrictions temporarily and observe whether all servers resume normal operation immediately",
                "score": 12
            },
            {
                "text": "Restart the storage-connected application servers to refresh any stale access tokens or sessions",
                "score": 11
            }
        ],
        "feedback": "The strongest first step is to inspect the actual permission and identity model that changed. Comparing a working and failing server is also a strong diagnostic move and can quickly narrow whether the problem is host-specific or identity-specific, but it follows the same root direction. Temporarily removing restrictions restores access at the expense of control and can weaken security. Restarts may refresh tokens but do not explain why only some servers fail.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_cloudsync_024",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 8}
        },
        "location": "helpdesk",
        "points": 41,
        "question": "A hybrid identity sync job completes, but some new on-prem changes never appear in the cloud directory. What should you investigate first?",
        "choices": [
            {
                "text": "Review sync scope, connector state, filtering rules, and the error path for the objects that are missing",
                "score": 41
            },
            {
                "text": "Compare one object that synced successfully and one that did not to identify which attribute or scope difference is blocking export",
                "score": 34
            },
            {
                "text": "Restart the sync server and run another full sync cycle before checking the connector details",
                "score": 14
            },
            {
                "text": "Create the missing cloud-side objects manually so the environments look aligned again",
                "score": 10
            }
        ],
        "feedback": "Checking sync scope, filters, and object-specific errors is the strongest first move because only some changes are missing. Comparing a working and missing object is also a strong method and helps isolate the exact differentiator, but it usually follows the connector and filter review. Restarting and forcing another sync may eventually help but does not explain the selective failure. Manual cloud creation risks divergence.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    },

    {
        "id": "hard_cert_025",
        "question_difficulty": "hard",
        "spawn_rules": {
            "easy": {"allowed": False, "weight": 0},
            "medium": {"allowed": False, "weight": 0},
            "hard": {"allowed": True, "weight": 10}
        },
        "location": "helpdesk",
        "points": 48,
        "question": "Mutual TLS authentication suddenly fails between two internal services after a certificate rollover, even though both services are up and reachable. What should you check first?",
        "choices": [
            {
                "text": "Review the new certificates, trust chain, mapping rules, and client or server certificate requirements used in the mutual TLS flow",
                "score": 48
            },
            {
                "text": "Compare the old and new certificates for SAN, EKU, issuer, and trust differences that could change how the two services validate one another",
                "score": 39
            },
            {
                "text": "Restart both services so the renewed certificates are reloaded from a clean state and then retest authentication",
                "score": 15
            },
            {
                "text": "Disable strict certificate validation temporarily so traffic can resume while the trust relationship is reviewed",
                "score": 4
            }
        ],
        "feedback": "The strongest answer checks the live certificate trust and mapping requirements actually used by the mutual TLS exchange. Comparing old and new certificates is also a strong diagnostic approach and may reveal what changed, but it follows slightly behind checking the currently active certificate and trust path first. Restarting services may be appropriate if certificates were not reloaded, but it is less direct than verifying the trust requirements. Disabling validation undermines the whole security model.",
        "allowed_days": [],
        "followup_event": {"allowed": False, "event_id": ""},
        "repeatable": False
    }

]