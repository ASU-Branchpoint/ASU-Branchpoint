#Full definition of all events in the game. Clunky, and only temporarily held in memory.
#TODO: -Multiple copies of events divided by department, assign departments to events.
#      -Fix extremely arbitrary weighting and point assigning for better random insertion.
#TO LIBRARY WRITER: Question difficulty should be capitalized unless secondary shorthand includes capitalized difficulty.
#                   Add a "secondary shorthand" that's longer than existing shorthand to make menus more understandable.
#                       Existing shorthand should remain for the notifications.
#                   defineHelpdesk , defineRD, defineOffice, defineCyber, defineCubicle, defineStorage, defineCopier
#           Thanks!
label defineFull:
    python:

        event_library = [

        {
            "id": "easy_sec_001",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 5,
            "question": "A user reports a pop-up claiming their computer is infected and instructing them to call a support number. What should you do first?",
            "choices": [
                {
                    "answerText": "Have the user stop interacting with the pop-up, disconnect if needed, and verify whether the alert came from approved security software",
                    "score": 5
                },
                {
                    "answerText": "Ask the user to close the browser, capture a screenshot, and continue working while monitoring for additional symptoms",
                    "score": 3
                },
                {
                    "answerText": "Call the number provided in the alert to confirm whether the message is legitimate and requires further action",
                    "score": 0
                }
            ],
            "feedback": "Stopping interaction and verifying the alert source is strongest because these pop-ups are commonly used for scams. Closing the browser and monitoring is reasonable but does not confirm whether anything executed. Calling the number is the weakest option because it directly engages with a likely attacker.",
            "shorthand": "Security Issue",
            "longhand": "Fake malware pop-up requests user action",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_acc_002",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 8,
            "question": "A user reports being locked out of their account without attempting to log in recently. What should you check first?",
            "choices": [
                {
                    "answerText": "Review authentication logs for repeated failed attempts and identify whether another system or source is using stale credentials",
                    "score": 8
                },
                {
                    "answerText": "Unlock the account and observe whether the lockout happens again while the user attempts to sign in normally",
                    "score": 5
                },
                {
                    "answerText": "Disable the account temporarily to prevent further access without determining what caused the lockout condition",
                    "score": 1
                }
            ],
            "feedback": "Reviewing logs is strongest because unexpected lockouts often indicate password attacks or misconfigured services. Unlocking and observing is reactive. Disabling the account without investigation disrupts access without identifying cause.",
            "shorthand": "Access Issue",
            "longhand": "Unexpected account lockout activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_003",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 6,
            "question": "A user reports receiving an email asking them to verify their login credentials through a link. What should you do first?",
            "choices": [
                {
                    "answerText": "Examine the email headers and link destination to determine whether the message is a phishing attempt before taking further action",
                    "score": 6
                },
                {
                    "answerText": "Ask the user to delete the email immediately and avoid interacting with it without performing further analysis",
                    "score": 3
                },
                {
                    "answerText": "Click the link in a browser to see whether the login page appears legitimate and matches the expected service",
                    "score": 0
                }
            ],
            "feedback": "Analyzing the email is strongest because it preserves evidence and confirms whether it is malicious. Deleting it removes immediate risk but loses forensic value. Clicking the link is the worst option because it may trigger compromise.",
            "shorthand": "Security Issue",
            "longhand": "Suspicious credential phishing email reported",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_004",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 7,
            "question": "A user plugs in an unknown USB device they found in the office. What should you do first?",
            "choices": [
                {
                    "answerText": "Disconnect the device immediately and check the system for unauthorized activity or malicious processes that may have executed",
                    "score": 7
                },
                {
                    "answerText": "Leave the device connected and monitor whether any unusual behavior occurs over time during normal system use",
                    "score": 3
                },
                {
                    "answerText": "Copy files from the device to inspect its contents and determine whether anything appears suspicious or out of place",
                    "score": 0
                }
            ],
            "feedback": "Removing the device is strongest because unknown USBs are a known attack vector. Monitoring while connected risks execution. Interacting with files directly increases exposure risk.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown USB device connected to system",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_005",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 9,
            "question": "A user reports receiving multiple login alerts from different geographic locations within a short period. What should you do first?",
            "choices": [
                {
                    "answerText": "Review authentication logs and immediately secure the account by enforcing a password reset and validating multi-factor authentication status",
                    "score": 9
                },
                {
                    "answerText": "Ask the user whether they were traveling or using a VPN service that might explain the unusual login locations",
                    "score": 4
                },
                {
                    "answerText": "Ignore the alerts since some services may report inaccurate location data under normal conditions",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs and securing the account is strongest because this pattern indicates compromise risk. Asking the user is useful but secondary. Ignoring alerts is weakest because it dismisses a clear warning sign.",
            "shorthand": "Access Issue",
            "longhand": "Multiple suspicious login alerts detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_006",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 7,
            "question": "A user clicked a suspicious link in an email but reports nothing happened. What should you do first?",
            "choices": [
                {
                    "answerText": "Check the system for indicators of compromise and review logs to determine whether any malicious activity was triggered by the click",
                    "score": 7
                },
                {
                    "answerText": "Restart the system and observe whether any unusual behavior occurs during normal use afterward",
                    "score": 3
                },
                {
                    "answerText": "Assume no action is needed because the user did not notice any visible changes on the system",
                    "score": 0
                }
            ],
            "feedback": "Checking for indicators of compromise is strongest because attacks may not show immediate signs. Restarting is less targeted but may reveal instability. Assuming nothing happened is weakest because it ignores potential silent compromise.",
            "shorthand": "Security Issue",
            "longhand": "User clicked phishing link",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_007",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 6,
            "question": "A user installs software from an unverified website without approval. What should you do first?",
            "choices": [
                {
                    "answerText": "Verify the legitimacy of the software, check for known malicious indicators, and remove it if it violates security policy",
                    "score": 6
                },
                {
                    "answerText": "Allow the software to remain installed while monitoring system performance and stability over time",
                    "score": 2
                },
                {
                    "answerText": "Deploy the same software to other systems so all users remain consistent with the installed applications",
                    "score": 0
                }
            ],
            "feedback": "Verifying and removing unauthorized software is strongest because it may introduce risk. Monitoring without validation is weaker. Deploying it elsewhere is the worst option because it spreads potential compromise.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unauthorized software installed on system",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_008",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 8},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCopier,
            "points": 4,
            "question": "Sensitive documents are found left unattended at a shared printer. What should you do first?",
            "choices": [
                {
                    "answerText": "Secure the documents immediately and identify the owner while reviewing whether any unauthorized individuals had access",
                    "score": 4
                },
                {
                    "answerText": "Leave the documents in place and wait for the original user to return and collect them without intervention",
                    "score": 2
                },
                {
                    "answerText": "Discard the documents without verifying their importance or attempting to identify the responsible user",
                    "score": 0
                }
            ],
            "feedback": "Securing documents is strongest because it prevents unauthorized access. Waiting leaves exposure risk. Discarding them may cause data loss and removes accountability.",
            "shorthand": "Data Issue",
            "longhand": "Sensitive documents left unattended",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_009",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 5,
            "question": "A user shares their password with a coworker to complete a task more quickly. What should you do first?",
            "choices": [
                {
                    "answerText": "Instruct the user to change their password immediately and reinforce security policies regarding credential sharing",
                    "score": 5
                },
                {
                    "answerText": "Allow the behavior temporarily since the task required urgent completion under time constraints",
                    "score": 2
                },
                {
                    "answerText": "Ignore the situation since both users are within the same department and likely trusted",
                    "score": 0
                }
            ],
            "feedback": "Resetting the password and reinforcing policy is strongest because credential sharing is a violation. Allowing it weakens controls. Ignoring it normalizes insecure behavior.",
            "shorthand": "Access Issue",
            "longhand": "User shares credentials with coworker",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_010",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 8,
            "question": "A user reports receiving an unexpected file attachment from an internal coworker. What should you do first?",
            "choices": [
                {
                    "answerText": "Verify with the sender through a separate communication channel and analyze the attachment before allowing it to be opened",
                    "score": 8
                },
                {
                    "answerText": "Ask the user to open the attachment in a sandboxed environment to observe whether anything unusual occurs during execution",
                    "score": 4
                },
                {
                    "answerText": "Assume it is safe because it originated from an internal account and allow the user to proceed without verification",
                    "score": 0
                }
            ],
            "feedback": "Verifying the sender and analyzing the attachment is strongest because accounts can be compromised. Sandbox testing is less safe. Assuming trust based on origin is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected internal attachment received",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_011",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 6,
            "question": "A user notices their browser homepage has changed without their input. What should you do first?",
            "choices": [
                {
                    "answerText": "Review browser extensions, recent installs, and system changes to determine whether unauthorized modifications were introduced",
                    "score": 6
                },
                {
                    "answerText": "Reset the homepage manually and continue working while monitoring for additional changes over time",
                    "score": 3
                },
                {
                    "answerText": "Ignore the change since browser updates may adjust settings automatically during normal operation",
                    "score": 0
                }
            ],
            "feedback": "Reviewing extensions and system changes is strongest because homepage hijacking is a common indicator of compromise. Resetting settings is reactive and does not address root cause. Ignoring the change is weakest because it dismisses a likely unauthorized modification.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unexpected browser homepage change",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_012",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 10,
            "question": "A user reports their account sent emails they did not write. What should you do first?",
            "choices": [
                {
                    "answerText": "Secure the account by resetting the password, reviewing sent messages, and checking for unauthorized login activity",
                    "score": 10
                },
                {
                    "answerText": "Ask the user to monitor their account and report if additional unauthorized emails are sent",
                    "score": 4
                },
                {
                    "answerText": "Ignore the report since delayed or cached messages can sometimes appear unexpectedly",
                    "score": 0
                }
            ],
            "feedback": "Securing the account is strongest because this indicates likely compromise. Monitoring is reactive and delays response. Ignoring it is weakest because it dismisses a critical indicator.",
            "shorthand": "Security Issue",
            "longhand": "Account sending unauthorized emails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_013",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 7,
            "question": "A user notices a program installed on their system that they do not recognize. What should you do first?",
            "choices": [
                {
                    "answerText": "Identify the program, verify its legitimacy, and review system activity to determine whether it was installed maliciously",
                    "score": 7
                },
                {
                    "answerText": "Leave the program installed and monitor whether it affects system behavior during normal operation",
                    "score": 3
                },
                {
                    "answerText": "Ignore the program since system updates may install additional components automatically",
                    "score": 0
                }
            ],
            "feedback": "Identifying and verifying the program is strongest because unknown software may indicate compromise. Monitoring is weaker because it delays action. Ignoring it is weakest because it overlooks potential risk.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown program installed",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_014",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 6,
            "question": "A user receives repeated password reset emails they did not request. What should you do first?",
            "choices": [
                {
                    "answerText": "Check account activity, secure the account with a password reset, and verify whether unauthorized attempts are being made",
                    "score": 6
                },
                {
                    "answerText": "Ask the user to ignore the emails unless they notice changes to their account access",
                    "score": 2
                },
                {
                    "answerText": "Disable password reset functionality for the account to prevent further notifications",
                    "score": 0
                }
            ],
            "feedback": "Checking activity and securing the account is strongest because reset attempts may indicate targeting. Ignoring is weaker and reactive. Disabling resets is weakest because it breaks functionality without solving the issue.",
            "shorthand": "Access Issue",
            "longhand": "Unrequested password reset emails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_015",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 9},
                "medium": {"allowed": True, "weight": 4},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 9,
            "question": "A user reports their system camera activated briefly without their input. What should you do first?",
            "choices": [
                {
                    "answerText": "Check running processes, application permissions, and system logs to determine whether unauthorized access occurred",
                    "score": 9
                },
                {
                    "answerText": "Restart the system and observe whether the issue happens again during normal usage",
                    "score": 3
                },
                {
                    "answerText": "Ignore the behavior since applications may briefly access hardware during updates",
                    "score": 0
                }
            ],
            "feedback": "Checking processes and permissions is strongest because unauthorized access may indicate spyware. Restarting is secondary. Ignoring is weakest because it dismisses a potential compromise.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unexpected camera activation",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_net_016",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineServer,
            "points": 8,
            "question": "A user reports frequent redirects when attempting to browse common websites. What should you check first?",
            "choices": [
                {
                    "answerText": "Check DNS settings, browser configuration, and network behavior to determine whether a redirect or hijack condition exists",
                    "score": 8
                },
                {
                    "answerText": "Ask the user to continue browsing and report whether the redirects become more frequent over time",
                    "score": 2
                },
                {
                    "answerText": "Ignore the issue since some websites may redirect users depending on region or content",
                    "score": 0
                }
            ],
            "feedback": "Checking DNS and browser configuration is strongest because redirects often indicate compromise. Monitoring is reactive. Ignoring is weakest because it dismisses a likely issue.",
            "shorthand": "Network Issue",
            "longhand": "Unexpected browser redirects",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_acc_017",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpdesk,
            "points": 9,
            "question": "A user reports their password no longer works even though they believe it is correct. What should you check first?",
            "choices": [
                {
                    "answerText": "Review authentication logs and account history to determine whether the password was changed or the account was modified",
                    "score": 9
                },
                {
                    "answerText": "Reset the password immediately and allow the user to regain access without checking recent activity",
                    "score": 4
                },
                {
                    "answerText": "Assume the user made a mistake and instruct them to retry their password multiple times",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because unexpected failure may indicate compromise. Resetting is reactive. Assuming user error is weakest because it ignores risk.",
            "shorthand": "Access Issue",
            "longhand": "Password unexpectedly invalid",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_data_018",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineStorage,
            "points": 7,
            "question": "A user notices a document they worked on has been modified without their input. What should you check first?",
            "choices": [
                {
                    "answerText": "Review file access logs and permissions to determine who accessed or modified the document and when the change occurred",
                    "score": 7
                },
                {
                    "answerText": "Restore the document from backup and continue working without identifying the source of the change",
                    "score": 3
                },
                {
                    "answerText": "Ignore the issue since version changes may occur automatically in shared environments",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because it identifies the cause. Restoring fixes symptoms. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Document modified unexpectedly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_019",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpdesk,
            "points": 5,
            "question": "A user receives a phone call asking for login credentials from someone claiming to be IT. What should you do first?",
            "choices": [
                {
                    "answerText": "Instruct the user not to share credentials and report the incident while confirming whether any information was already disclosed",
                    "score": 5
                },
                {
                    "answerText": "Ask the user to call the number back to verify whether the request was legitimate",
                    "score": 0
                },
                {
                    "answerText": "Advise the user to ignore the call and continue working without reporting the incident",
                    "score": 2
                }
            ],
            "feedback": "Reporting and preventing disclosure is strongest because this is social engineering. Calling back is unsafe. Ignoring without reporting is weaker.",
            "shorthand": "Security Issue",
            "longhand": "Credential phishing phone call",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_end_020",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineCubicle,
            "points": 6,
            "question": "A user reports frequent pop-up advertisements appearing on their system during normal use. What should you do first?",
            "choices": [
                {
                    "answerText": "Check for adware by reviewing installed applications, extensions, and recent downloads that may have introduced unwanted software",
                    "score": 6
                },
                {
                    "answerText": "Close the pop-ups and continue working while monitoring whether the issue persists",
                    "score": 2
                },
                {
                    "answerText": "Ignore the behavior since advertisements may appear during normal browsing activity",
                    "score": 0
                }
            ],
            "feedback": "Checking for adware is strongest because pop-ups often indicate unwanted software. Closing is temporary. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Frequent pop-up advertisements",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_data_021",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineStorage,
            "points": 8,
            "question": "A removable storage device containing company data is reported missing. What should you do first?",
            "choices": [
                {
                    "answerText": "Report the incident, determine what data was on the device, and assess whether sensitive information may have been exposed",
                    "score": 8
                },
                {
                    "answerText": "Wait to see if the device is returned before taking further action",
                    "score": 2
                },
                {
                    "answerText": "Ignore the situation since removable devices are often misplaced temporarily",
                    "score": 0
                }
            ],
            "feedback": "Reporting and assessing exposure is strongest. Waiting delays response. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Missing removable storage device",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_end_022",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineCubicle,
            "points": 9,
            "question": "A user notices their microphone is being accessed without their interaction. What should you do first?",
            "choices": [
                {
                    "answerText": "Check active processes, permissions, and logs to determine whether any unauthorized application accessed the microphone",
                    "score": 9
                },
                {
                    "answerText": "Restart the system and monitor whether the issue happens again during normal use",
                    "score": 3
                },
                {
                    "answerText": "Ignore the behavior since applications may briefly access hardware during updates",
                    "score": 0
                }
            ],
            "feedback": "Checking processes is strongest because this may indicate spyware. Restarting is secondary. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unexpected microphone access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_acc_023",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpdesk,
            "points": 10,
            "question": "A user entered their credentials into a suspicious website. What should you do first?",
            "choices": [
                {
                    "answerText": "Immediately reset the password, review account activity, and enforce additional protections such as multi-factor authentication",
                    "score": 10
                },
                {
                    "answerText": "Ask the user to monitor their account for suspicious activity and report if anything unusual occurs",
                    "score": 3
                },
                {
                    "answerText": "Ignore the situation since the user recognized the mistake quickly",
                    "score": 0
                }
            ],
            "feedback": "Resetting credentials is strongest because they may already be compromised. Monitoring is reactive. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Credentials entered into phishing site",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_end_024",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineCubicle,
            "points": 7,
            "question": "A user notices an unknown browser extension installed without their knowledge. What should you do first?",
            "choices": [
                {
                    "answerText": "Identify the extension, verify its origin, and remove it while checking for related unauthorized changes",
                    "score": 7
                },
                {
                    "answerText": "Disable the extension temporarily and continue working while observing system behavior",
                    "score": 3
                },
                {
                    "answerText": "Ignore the extension since browsers may install components automatically",
                    "score": 0
                }
            ],
            "feedback": "Identifying and removing is strongest because it may be malicious. Disabling is partial mitigation. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown browser extension installed",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "easy_sec_025",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 10},
                "medium": {"allowed": False, "weight": 0},
                "hard": {"allowed": True, "weight": 3}
            },
            "location": defineHelpdesk,
            "points": 6,
            "question": "A user reports a sudden increase in spam emails reaching their inbox. What should you check first?",
            "choices": [
                {
                    "answerText": "Review email filtering rules and sender patterns to determine whether spam controls are failing or being bypassed",
                    "score": 6
                },
                {
                    "answerText": "Ask the user to delete the emails and monitor whether the volume decreases over time",
                    "score": 3
                },
                {
                    "answerText": "Disable spam filtering temporarily to test whether the system is misclassifying messages",
                    "score": 0
                }
            ],
            "feedback": "Reviewing filtering is strongest because it identifies control failures. Deleting is reactive. Disabling filtering is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Sudden spike in spam emails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_001",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineCyber,
            "points": 22,
            "question": "Multiple users report receiving similar phishing emails that bypassed spam filters. What should you check first?",
            "choices": [
                {
                    "answerText": "Review email filtering rules, analyze message headers, and determine why the phishing campaign bypassed existing detection controls",
                    "score": 22
                },
                {
                    "answerText": "Instruct users to delete the emails and report future messages while monitoring whether the campaign continues",
                    "score": 10
                },
                {
                    "answerText": "Block the sender domain immediately without reviewing how the messages avoided detection mechanisms",
                    "score": 4
                },
                {
                    "answerText": "Ignore the situation since some phishing emails may occasionally bypass filters without indicating a larger issue",
                    "score": 0
                }
            ],
            "feedback": "Analyzing filtering and headers is strongest because it identifies why controls failed. Deleting emails is reactive. Blocking domains helps but skips root cause. Ignoring it is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Phishing campaign bypasses email filtering",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_acc_002",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineCyber,
            "points": 24,
            "question": "Authentication logs show repeated successful logins from an unfamiliar IP address for a single user. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate login patterns, confirm whether the activity aligns with user behavior, and verify whether credentials were compromised",
                    "score": 24
                },
                {
                    "answerText": "Ask the user if they recently traveled or used a VPN that could explain the unfamiliar login source",
                    "score": 14
                },
                {
                    "answerText": "Reset the password without reviewing logs and assume the activity was unauthorized",
                    "score": 6
                },
                {
                    "answerText": "Ignore the log entries since IP addresses may change frequently depending on user location",
                    "score": 0
                }
            ],
            "feedback": "Investigating patterns is strongest because it determines legitimacy and scope. Asking the user is useful but secondary. Resetting without review skips analysis. Ignoring logs is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Unusual successful logins detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_net_003",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineServer,
            "points": 21,
            "question": "Users report intermittent access to internal services while external access remains stable. What should you check first?",
            "choices": [
                {
                    "answerText": "Review internal network routing, DNS resolution, and service availability to identify inconsistencies affecting internal access",
                    "score": 21
                },
                {
                    "answerText": "Restart affected systems and observe whether access stabilizes without identifying the root cause",
                    "score": 9
                },
                {
                    "answerText": "Assume the issue is temporary and monitor whether it resolves without further investigation",
                    "score": 0
                }
            ],
            "feedback": "Reviewing routing and DNS is strongest because the issue is internal-specific. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Intermittent internal service access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_end_004",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineRD,
            "points": 26,
            "question": "An endpoint detection system flags unusual process behavior on a workstation. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze the process activity, review execution history, and determine whether the behavior matches known malicious patterns",
                    "score": 26
                },
                {
                    "answerText": "Restart the workstation and verify whether the alert appears again during normal usage",
                    "score": 11
                },
                {
                    "answerText": "Disable the detection alert and assume the activity is a false positive without investigation",
                    "score": 0
                }
            ],
            "feedback": "Analyzing process behavior is strongest because it determines whether the alert is valid. Restarting is reactive. Ignoring alerts is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Suspicious process behavior detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_data_005",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineStorage,
            "points": 23,
            "question": "Audit logs show a large number of file downloads from a shared drive by a single user. What should you check first?",
            "choices": [
                {
                    "answerText": "Review access patterns, confirm whether the downloads align with job responsibilities, and assess potential data exfiltration risk",
                    "score": 23
                },
                {
                    "answerText": "Ask the user if the downloads were necessary and continue monitoring for further activity",
                    "score": 12
                },
                {
                    "answerText": "Ignore the activity since users may download files in bulk for legitimate work purposes",
                    "score": 0
                }
            ],
            "feedback": "Reviewing patterns is strongest because it identifies intent and risk. Asking the user is secondary. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Unusual bulk file download activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_006",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 18,
            "question": "A user reports receiving repeated MFA prompts they did not initiate. What should you check first?",
            "choices": [
                {
                    "answerText": "Review authentication logs, verify whether login attempts are occurring, and determine whether the account is being targeted",
                    "score": 18
                },
                {
                    "answerText": "Ask the user to ignore the prompts and report if they continue to receive them over time",
                    "score": 7
                },
                {
                    "answerText": "Disable MFA temporarily to stop the prompts from appearing on the user's device",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because MFA prompts indicate active login attempts. Ignoring is weaker. Disabling MFA is worst.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected MFA prompt activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_net_007",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineServer,
            "points": 20,
            "question": "Network monitoring shows a spike in outbound traffic from a single host. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze the traffic destination, volume, and process generating the traffic to determine whether data exfiltration is occurring",
                    "score": 20
                },
                {
                    "answerText": "Restart the host and monitor whether outbound traffic returns to normal levels",
                    "score": 8
                },
                {
                    "answerText": "Ignore the spike since network usage may fluctuate depending on normal activity patterns",
                    "score": 0
                }
            ],
            "feedback": "Analyzing traffic is strongest because it identifies potential exfiltration. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Unusual outbound traffic spike",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_acc_008",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 19,
            "question": "A user reports they suddenly gained access to a system they should not have permissions for. What should you check first?",
            "choices": [
                {
                    "answerText": "Review access control changes, group memberships, and recent permission updates to determine how access was granted",
                    "score": 19
                },
                {
                    "answerText": "Remove the access immediately and continue without reviewing how the permissions were assigned",
                    "score": 8
                },
                {
                    "answerText": "Ignore the issue since temporary access may have been granted for operational reasons",
                    "score": 0
                }
            ],
            "feedback": "Reviewing permission changes is strongest because it identifies the root cause. Removing access is reactive. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Unexpected privilege escalation",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_end_009",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 17,
            "question": "An endpoint begins executing unknown scheduled tasks without user interaction. What should you check first?",
            "choices": [
                {
                    "answerText": "Review scheduled tasks, associated executables, and system logs to determine whether malicious persistence mechanisms exist",
                    "score": 17
                },
                {
                    "answerText": "Disable the tasks and monitor whether they reappear without investigating their origin",
                    "score": 7
                },
                {
                    "answerText": "Ignore the tasks since system updates may create scheduled processes automatically",
                    "score": 0
                }
            ],
            "feedback": "Reviewing tasks and logs is strongest because it identifies persistence mechanisms. Disabling is reactive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown scheduled tasks executing",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_data_010",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 3},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineStorage,
            "points": 25,
            "question": "Backup logs show several critical systems were not included in the last scheduled backup. What should you check first?",
            "choices": [
                {
                    "answerText": "Review backup configuration, system inclusion rules, and recent changes to determine why systems were excluded",
                    "score": 25
                },
                {
                    "answerText": "Run a new backup immediately without reviewing the cause of the exclusion",
                    "score": 12
                },
                {
                    "answerText": "Ignore the logs since backups may occasionally skip systems without indicating a larger issue",
                    "score": 0
                }
            ],
            "feedback": "Reviewing configuration is strongest because it identifies the failure cause. Running backups is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Critical systems missing from backups",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_011",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineCyber,
            "points": 27,
            "question": "Security logs show multiple failed login attempts followed by a successful login for a privileged account. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze authentication logs, correlate timestamps, and determine whether the successful login originated from the same source as the failed attempts",
                    "score": 27
                },
                {
                    "answerText": "Reset the account password immediately and continue monitoring for additional suspicious login attempts",
                    "score": 15
                },
                {
                    "answerText": "Ignore the failed attempts since users may occasionally mistype credentials before successfully logging in",
                    "score": 0
                }
            ],
            "feedback": "Analyzing logs is strongest because it determines whether brute force activity succeeded. Resetting is reactive. Ignoring is weakest because it overlooks a likely attack pattern.",
            "shorthand": "Security Issue",
            "longhand": "Brute force followed by successful login",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_net_012",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineServer,
            "points": 21,
            "question": "Network monitoring shows repeated connections to an unknown external IP from multiple internal systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze the destination IP, connection patterns, and originating processes to determine whether the traffic indicates command and control activity",
                    "score": 21
                },
                {
                    "answerText": "Block the external IP address and observe whether the connection attempts continue from internal systems",
                    "score": 12
                },
                {
                    "answerText": "Ignore the traffic since external connections are common in normal network operations",
                    "score": 0
                }
            ],
            "feedback": "Analyzing traffic is strongest because it identifies potential compromise. Blocking helps but skips investigation. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Multiple systems contacting unknown external IP",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_end_013",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineRD,
            "points": 24,
            "question": "Endpoint logs show a process spawning multiple child processes with unusual behavior. What should you check first?",
            "choices": [
                {
                    "answerText": "Review process lineage, execution context, and behavior patterns to determine whether the activity aligns with known malicious techniques",
                    "score": 24
                },
                {
                    "answerText": "Terminate the processes immediately and monitor whether similar activity occurs again",
                    "score": 13
                },
                {
                    "answerText": "Ignore the activity since complex applications may spawn multiple processes during normal operation",
                    "score": 0
                }
            ],
            "feedback": "Analyzing process lineage is strongest because it identifies malicious execution chains. Terminating is reactive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Suspicious process spawning activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_data_014",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineStorage,
            "points": 20,
            "question": "A shared folder shows a large number of files renamed in a short period. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate file activity logs and determine whether the pattern matches ransomware or automated modification behavior",
                    "score": 20
                },
                {
                    "answerText": "Restore files from backup and continue monitoring for additional changes",
                    "score": 11
                },
                {
                    "answerText": "Ignore the activity since bulk renaming may occur during legitimate file organization",
                    "score": 0
                }
            ],
            "feedback": "Investigating logs is strongest because mass renaming may indicate ransomware. Restoring is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Mass file renaming activity detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_acc_015",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineCyber,
            "points": 23,
            "question": "An account suddenly gains administrative privileges without a recorded request. What should you check first?",
            "choices": [
                {
                    "answerText": "Review privilege escalation logs, group membership changes, and administrative actions to determine how access was granted",
                    "score": 23
                },
                {
                    "answerText": "Remove administrative privileges immediately and monitor whether access is reassigned again",
                    "score": 12
                },
                {
                    "answerText": "Ignore the change since temporary privilege assignments may occur during system maintenance",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because it identifies unauthorized escalation. Removing access is reactive. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Unexpected administrative privilege assignment",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_016",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location": defineCyber,
            "points": 26,
            "question": "An alert indicates potential credential dumping activity on a system. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze system memory access patterns, process behavior, and security logs to confirm whether credential dumping techniques were used",
                    "score": 26
                },
                {
                    "answerText": "Restart the system and monitor whether similar alerts appear again during operation",
                    "score": 12
                },
                {
                    "answerText": "Ignore the alert since some administrative tools may access credentials during normal operation",
                    "score": 0
                }
            ],
            "feedback": "Analyzing memory and logs is strongest because credential dumping is a critical threat. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Potential credential dumping detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_net_017",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineServer,
            "points": 18,
            "question": "A system is generating a large number of DNS queries to random domains. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze DNS query patterns, domain reputation, and originating processes to determine whether the behavior indicates malware activity",
                    "score": 18
                },
                {
                    "answerText": "Restart the system and observe whether DNS activity returns to normal levels",
                    "score": 8
                },
                {
                    "answerText": "Ignore the behavior since DNS queries may vary depending on application usage",
                    "score": 0
                }
            ],
            "feedback": "Analyzing DNS patterns is strongest because random queries may indicate malware. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "High volume random DNS queries",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_end_018",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 17,
            "question": "An endpoint begins disabling security services without user input. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate system logs, process activity, and privilege usage to determine what is disabling the security controls",
                    "score": 17
                },
                {
                    "answerText": "Re-enable the services and monitor whether they are disabled again",
                    "score": 8
                },
                {
                    "answerText": "Ignore the behavior since system updates may temporarily disable services",
                    "score": 0
                }
            ],
            "feedback": "Investigating cause is strongest because disabling security controls indicates compromise. Re-enabling is reactive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Security services disabled unexpectedly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_data_019",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineStorage,
            "points": 19,
            "question": "Audit logs show a user accessing sensitive files outside of normal working hours. What should you check first?",
            "choices": [
                {
                    "answerText": "Review access logs, correlate timestamps with user activity, and determine whether the behavior aligns with legitimate use",
                    "score": 19
                },
                {
                    "answerText": "Ask the user whether they accessed the files and continue monitoring for additional activity",
                    "score": 9
                },
                {
                    "answerText": "Ignore the activity since users may occasionally work outside normal hours",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because it validates legitimacy. Asking is secondary. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "After-hours sensitive file access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_020",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 16,
            "question": "A user reports that a website they frequently use now has a certificate warning. What should you check first?",
            "choices": [
                {
                    "answerText": "Validate the certificate details, issuer, and domain consistency to determine whether the warning indicates a potential man-in-the-middle attack",
                    "score": 16
                },
                {
                    "answerText": "Ask the user to proceed past the warning and report whether the site behaves normally",
                    "score": 6
                },
                {
                    "answerText": "Ignore the warning since certificates may expire or change periodically",
                    "score": 0
                }
            ],
            "feedback": "Validating the certificate is strongest because warnings may indicate interception. Proceeding is risky. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected certificate warning",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_021",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 14,
            "question": "A user reports their system antivirus was turned off without their action. What should you check first?",
            "choices": [
                {
                    "answerText": "Review system logs and process activity to determine what disabled the antivirus service and whether malicious activity is present",
                    "score": 14
                },
                {
                    "answerText": "Re-enable antivirus and monitor whether it is disabled again during system use",
                    "score": 6
                },
                {
                    "answerText": "Ignore the issue since antivirus updates may temporarily disable protection features",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because disabling antivirus is a major indicator of compromise. Re-enabling is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Antivirus disabled unexpectedly",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_net_022",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineServer,
            "points": 15,
            "question": "Internal systems are intermittently failing to resolve domain names. What should you check first?",
            "choices": [
                {
                    "answerText": "Review DNS server health, query logs, and resolution paths to determine whether failures are due to configuration or service issues",
                    "score": 15
                },
                {
                    "answerText": "Restart affected systems and monitor whether name resolution improves during normal operation",
                    "score": 6
                },
                {
                    "answerText": "Ignore the issue since DNS failures may occur occasionally during network activity",
                    "score": 0
                }
            ],
            "feedback": "Reviewing DNS is strongest because the issue is resolution-specific. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Intermittent DNS resolution failures",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_end_023",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineCubicle,
            "points": 13,
            "question": "An endpoint shows signs of multiple failed application launches followed by one successful execution. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze execution logs and process behavior to determine whether the successful launch indicates malicious activity",
                    "score": 13
                },
                {
                    "answerText": "Restart the endpoint and monitor whether application launches normalize during use",
                    "score": 6
                },
                {
                    "answerText": "Ignore the behavior since applications may fail to start occasionally due to system conditions",
                    "score": 0
                }
            ],
            "feedback": "Analyzing logs is strongest because repeated failures followed by success may indicate exploitation attempts. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Repeated application launch failures then success",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_data_024",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineStorage,
            "points": 12,
            "question": "A backup verification report shows inconsistencies in file integrity checks. What should you check first?",
            "choices": [
                {
                    "answerText": "Review backup logs, integrity verification processes, and storage conditions to determine why inconsistencies occurred",
                    "score": 12
                },
                {
                    "answerText": "Run another backup and monitor whether inconsistencies continue to appear",
                    "score": 5
                },
                {
                    "answerText": "Ignore the report since minor inconsistencies may not affect overall data recovery",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because integrity issues may indicate corruption or tampering. Re-running backups is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Backup integrity inconsistencies detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "medium_sec_025",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": False, "weight": 0}
            },
            "location": defineHelpdesk,
            "points": 11,
            "question": "A user reports receiving a security alert about a login attempt from a foreign country. What should you check first?",
            "choices": [
                {
                    "answerText": "Review login activity, confirm whether the attempt was successful, and determine whether additional suspicious activity occurred",
                    "score": 11
                },
                {
                    "answerText": "Ask the user to change their password and monitor for additional alerts",
                    "score": 5
                },
                {
                    "answerText": "Ignore the alert since location data may sometimes be inaccurate",
                    "score": 0
                }
            ],
            "feedback": "Reviewing login activity is strongest because it confirms compromise status. Resetting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Foreign login attempt alert",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_001",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 45,
            "question": "Security logs indicate lateral movement activity between multiple internal hosts using valid credentials. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate authentication logs, host activity, and credential usage patterns to determine how the attacker is moving between systems",
                    "score": 45
                },
                {
                    "answerText": "Reset all potentially affected credentials and monitor whether lateral movement attempts continue across the environment",
                    "score": 30
                },
                {
                    "answerText": "Isolate one affected host and observe whether additional systems begin showing similar activity patterns",
                    "score": 18
                },
                {
                    "answerText": "Ignore the activity since legitimate administrative actions may involve accessing multiple systems",
                    "score": 0
                }
            ],
            "feedback": "Correlating logs is strongest because it reveals the attack path and scope. Resetting credentials helps contain but does not explain movement. Isolating a host is partial. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Detected lateral movement using valid credentials",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_002",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineServer,
            "points": 42,
            "question": "Network monitoring reveals beaconing behavior from multiple internal systems to a single external IP at regular intervals. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze traffic patterns, inspect payload characteristics, and identify processes generating the connections to confirm command and control activity",
                    "score": 42
                },
                {
                    "answerText": "Block the external IP address and monitor whether the beaconing behavior stops across all affected systems",
                    "score": 28
                },
                {
                    "answerText": "Restart affected systems and observe whether the network behavior changes during normal operation",
                    "score": 15
                },
                {
                    "answerText": "Ignore the traffic since periodic connections may occur due to legitimate application updates",
                    "score": 0
                }
            ],
            "feedback": "Analyzing beaconing is strongest because it identifies command and control. Blocking helps contain but skips root cause. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Beaconing to external command and control",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_acc_003",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 48,
            "question": "Privileged account activity shows access to multiple high-value systems outside normal patterns. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate access logs, session data, and privilege escalation activity to determine whether the account is compromised or being misused",
                    "score": 48
                },
                {
                    "answerText": "Disable the account immediately and monitor whether similar activity occurs using other accounts",
                    "score": 32
                },
                {
                    "answerText": "Ask the account owner to confirm whether the activity was legitimate and continue monitoring",
                    "score": 18
                },
                {
                    "answerText": "Ignore the behavior since administrators may access multiple systems during routine operations",
                    "score": 0
                }
            ],
            "feedback": "Correlating logs is strongest because it identifies compromise scope. Disabling is containment but lacks context. Asking is secondary. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Abnormal privileged account activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_end_004",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineRD,
            "points": 44,
            "question": "Endpoint telemetry indicates persistence mechanisms are being established after initial compromise. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate registry changes, scheduled tasks, and startup processes to identify persistence mechanisms and how they were deployed",
                    "score": 44
                },
                {
                    "answerText": "Remove identified persistence entries and monitor whether they are recreated by the system",
                    "score": 30
                },
                {
                    "answerText": "Reimage the system and verify whether the issue reappears on the endpoint",
                    "score": 18
                },
                {
                    "answerText": "Ignore the activity since system configuration changes may occur during updates",
                    "score": 0
                }
            ],
            "feedback": "Investigating persistence is strongest because it identifies attacker foothold. Removing entries is reactive. Reimaging is disruptive without context. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Persistence mechanisms detected post-compromise",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_data_005",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineStorage,
            "points": 46,
            "question": "Large volumes of sensitive data are being transferred to an external destination over encrypted channels. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze transfer patterns, encryption context, and originating processes to determine whether the activity represents data exfiltration",
                    "score": 46
                },
                {
                    "answerText": "Block the external destination and monitor whether data transfer attempts continue from internal systems",
                    "score": 30
                },
                {
                    "answerText": "Notify the user responsible for the system and ask whether the transfers were authorized",
                    "score": 18
                },
                {
                    "answerText": "Ignore the activity since encrypted transfers are commonly used for legitimate data exchange",
                    "score": 0
                }
            ],
            "feedback": "Analyzing transfer context is strongest because it identifies exfiltration. Blocking is containment. Asking is secondary. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Potential encrypted data exfiltration",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_006",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 41,
            "question": "An alert indicates suspicious PowerShell execution across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Review command history, execution context, and script content to determine whether the activity matches known attack techniques",
                    "score": 41
                },
                {
                    "answerText": "Disable PowerShell execution and monitor whether similar activity appears using alternate methods",
                    "score": 26
                },
                {
                    "answerText": "Restart affected systems and observe whether PowerShell activity resumes during normal operation",
                    "score": 14
                },
                {
                    "answerText": "Ignore the alert since administrators may use PowerShell for routine system management",
                    "score": 0
                }
            ],
            "feedback": "Analyzing execution is strongest because PowerShell is a common attack vector. Disabling is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Suspicious PowerShell activity detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_007",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineServer,
            "points": 39,
            "question": "Internal systems are experiencing DNS tunneling behavior based on query patterns. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze DNS query structure, frequency, and encoded payloads to confirm whether tunneling is being used for data exfiltration",
                    "score": 39
                },
                {
                    "answerText": "Block suspicious domains and monitor whether query behavior changes across affected systems",
                    "score": 25
                },
                {
                    "answerText": "Restart DNS services and observe whether query patterns normalize",
                    "score": 12
                },
                {
                    "answerText": "Ignore the activity since DNS queries may vary depending on application usage",
                    "score": 0
                }
            ],
            "feedback": "Analyzing DNS queries is strongest because it confirms tunneling. Blocking is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "DNS tunneling behavior detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_end_008",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineRD,
            "points": 37,
            "question": "An endpoint shows evidence of fileless malware activity with no persistent files on disk. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze memory artifacts, process injections, and runtime behavior to determine how the malware is executing without disk presence",
                    "score": 37
                },
                {
                    "answerText": "Restart the system and monitor whether suspicious behavior reappears after reboot",
                    "score": 20
                },
                {
                    "answerText": "Deploy antivirus scans and rely on signature detection to identify the threat",
                    "score": 10
                },
                {
                    "answerText": "Ignore the alert since lack of files suggests no persistent compromise",
                    "score": 0
                }
            ],
            "feedback": "Analyzing memory is strongest because fileless malware resides in memory. Restarting is temporary. Antivirus is limited. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Fileless malware activity detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_data_009",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineStorage,
            "points": 50,
            "question": "Sensitive database records are being accessed and modified in a pattern inconsistent with application behavior. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze database queries, user access patterns, and application logs to determine whether unauthorized manipulation is occurring",
                    "score": 50
                },
                {
                    "answerText": "Revert database changes and monitor whether modifications continue to occur",
                    "score": 32
                },
                {
                    "answerText": "Restrict database access temporarily and observe whether normal operations are impacted",
                    "score": 18
                },
                {
                    "answerText": "Ignore the activity since database operations may vary depending on application usage",
                    "score": 0
                }
            ],
            "feedback": "Analyzing queries is strongest because it identifies unauthorized manipulation. Reverting is reactive. Restricting is disruptive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Unauthorized database modification patterns",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_010",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 43,
            "question": "An attacker is suspected of using living-off-the-land techniques to evade detection. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate system logs, command execution history, and legitimate tool usage patterns to identify misuse of built-in utilities",
                    "score": 43
                },
                {
                    "answerText": "Disable commonly abused tools and monitor whether the attacker shifts to alternate techniques",
                    "score": 28
                },
                {
                    "answerText": "Reimage affected systems and verify whether suspicious behavior returns afterward",
                    "score": 16
                },
                {
                    "answerText": "Ignore the activity since legitimate tools are commonly used during normal operations",
                    "score": 0
                }
            ],
            "feedback": "Correlating logs is strongest because LOTL attacks blend with normal activity. Disabling tools is containment. Reimaging is disruptive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Living-off-the-land attack techniques detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_011",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 47,
            "question": "Security logs show suspicious use of built-in administrative tools across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate command execution logs, tool usage patterns, and user activity to identify whether legitimate utilities are being abused for malicious purposes",
                    "score": 47
                },
                {
                    "answerText": "Disable commonly used administrative tools and monitor whether suspicious activity shifts to other methods",
                    "score": 30
                },
                {
                    "answerText": "Restart affected systems and observe whether tool usage patterns return to normal behavior",
                    "score": 15
                },
                {
                    "answerText": "Ignore the activity since administrators frequently use built-in tools during routine operations",
                    "score": 0
                }
            ],
            "feedback": "Correlating logs is strongest because it identifies living-off-the-land abuse. Disabling tools is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Abuse of legitimate administrative tools detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_012",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineServer,
            "points": 40,
            "question": "Network traffic analysis shows encrypted outbound connections to multiple unknown destinations from a critical server. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze connection endpoints, process origins, and traffic patterns to determine whether the server is participating in unauthorized communications",
                    "score": 40
                },
                {
                    "answerText": "Block outbound connections from the server and observe whether application functionality is impacted",
                    "score": 28
                },
                {
                    "answerText": "Restart the server and monitor whether outbound traffic patterns change during normal operation",
                    "score": 14
                },
                {
                    "answerText": "Ignore the connections since encrypted communication is commonly used by legitimate services",
                    "score": 0
                }
            ],
            "feedback": "Analyzing traffic is strongest because it identifies potential compromise. Blocking is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Suspicious encrypted outbound traffic from server",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_acc_013",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 49,
            "question": "An attacker is suspected of harvesting credentials through memory access techniques. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze memory access patterns, privileged process activity, and credential storage interactions to confirm whether harvesting techniques are being used",
                    "score": 49
                },
                {
                    "answerText": "Reset all user credentials and monitor whether authentication anomalies continue to appear",
                    "score": 32
                },
                {
                    "answerText": "Restart affected systems and observe whether suspicious activity resumes during operation",
                    "score": 18
                },
                {
                    "answerText": "Ignore the suspicion since credential access is part of normal system authentication processes",
                    "score": 0
                }
            ],
            "feedback": "Analyzing memory is strongest because credential harvesting often occurs in memory. Resetting credentials is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Credential harvesting via memory access suspected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_end_014",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineRD,
            "points": 38,
            "question": "Endpoint telemetry shows process injection behavior across several systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate process relationships, memory injection patterns, and execution context to determine how malicious code is being inserted",
                    "score": 38
                },
                {
                    "answerText": "Terminate affected processes and monitor whether injection behavior reappears during system use",
                    "score": 24
                },
                {
                    "answerText": "Reimage the systems and verify whether similar behavior occurs again",
                    "score": 14
                },
                {
                    "answerText": "Ignore the behavior since complex applications may interact with multiple processes",
                    "score": 0
                }
            ],
            "feedback": "Investigating injection is strongest because it reveals execution techniques. Terminating is reactive. Reimaging is disruptive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Process injection behavior detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_data_015",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineStorage,
            "points": 41,
            "question": "Data integrity monitoring shows unauthorized changes to critical configuration files. What should you check first?",
            "choices": [
                {
                    "answerText": "Review file integrity logs, access history, and system changes to determine who modified the files and how the changes occurred",
                    "score": 41
                },
                {
                    "answerText": "Restore the configuration files from backup and monitor whether unauthorized changes occur again",
                    "score": 26
                },
                {
                    "answerText": "Restrict access to the files and observe whether system functionality is impacted",
                    "score": 15
                },
                {
                    "answerText": "Ignore the changes since configuration files may be updated during maintenance",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because it identifies unauthorized changes. Restoring is reactive. Restricting is disruptive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Unauthorized modification of configuration files",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_016",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 44,
            "question": "An attacker is suspected of using token impersonation to access resources. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze token usage patterns, session activity, and privilege escalation behavior to determine whether impersonation techniques are being used",
                    "score": 44
                },
                {
                    "answerText": "Revoke active sessions and monitor whether unauthorized access attempts continue across systems",
                    "score": 28
                },
                {
                    "answerText": "Reset user passwords and observe whether suspicious access patterns persist",
                    "score": 16
                },
                {
                    "answerText": "Ignore the activity since tokens are used frequently in normal authentication processes",
                    "score": 0
                }
            ],
            "feedback": "Analyzing token usage is strongest because impersonation is difficult to detect. Revoking sessions is containment. Resetting passwords is partial. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Token impersonation suspected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_017",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineServer,
            "points": 36,
            "question": "Internal traffic analysis shows abnormal segmentation bypass between restricted network zones. What should you check first?",
            "choices": [
                {
                    "answerText": "Review firewall rules, segmentation policies, and traffic logs to determine how unauthorized communication paths are being established",
                    "score": 36
                },
                {
                    "answerText": "Block traffic between affected zones and monitor whether communication attempts continue",
                    "score": 24
                },
                {
                    "answerText": "Restart network devices and observe whether segmentation behavior returns to normal",
                    "score": 12
                },
                {
                    "answerText": "Ignore the activity since network traffic may occasionally cross boundaries during legitimate operations",
                    "score": 0
                }
            ],
            "feedback": "Reviewing segmentation is strongest because it identifies control failure. Blocking is containment. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Network segmentation bypass detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_end_018",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineRD,
            "points": 37,
            "question": "Multiple endpoints exhibit signs of memory-resident malware spreading without file artifacts. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze memory structures, process injection behavior, and inter-process communication to determine how the malware propagates",
                    "score": 37
                },
                {
                    "answerText": "Restart affected systems and monitor whether the malware behavior reappears after reboot",
                    "score": 22
                },
                {
                    "answerText": "Deploy antivirus scans and rely on signature detection to identify the threat",
                    "score": 12
                },
                {
                    "answerText": "Ignore the activity since no files are present on disk to indicate compromise",
                    "score": 0
                }
            ],
            "feedback": "Analyzing memory is strongest because fileless malware operates in memory. Restarting is temporary. Antivirus is limited. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Fileless malware spreading across endpoints",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_data_019",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineStorage,
            "points": 39,
            "question": "A database shows signs of slow, stealthy data extraction over an extended period. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze query patterns, access frequency, and data access logs to identify whether extraction techniques are being used covertly",
                    "score": 39
                },
                {
                    "answerText": "Restrict database access temporarily and monitor whether extraction activity stops",
                    "score": 25
                },
                {
                    "answerText": "Revert database changes and observe whether anomalies continue to appear",
                    "score": 14
                },
                {
                    "answerText": "Ignore the activity since database access patterns may vary over time",
                    "score": 0
                }
            ],
            "feedback": "Analyzing query patterns is strongest because it identifies stealth exfiltration. Restricting is containment. Reverting is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Stealthy long-term data extraction detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_020",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 2},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 43,
            "question": "Security alerts indicate that logging mechanisms are being tampered with across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze log integrity, access controls, and system changes to determine how logging is being altered or suppressed",
                    "score": 43
                },
                {
                    "answerText": "Restore logging configurations and monitor whether tampering continues across affected systems",
                    "score": 27
                },
                {
                    "answerText": "Restart systems and observe whether logs begin recording normally again",
                    "score": 15
                },
                {
                    "answerText": "Ignore the issue since logging disruptions may occur during system updates",
                    "score": 0
                }
            ],
            "feedback": "Analyzing integrity is strongest because attackers often disable logs to evade detection. Restoring is reactive. Restarting is temporary. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Log tampering across multiple systems",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_acc_021",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineOffice,
            "points": 50,
            "question": "An attacker is suspected of maintaining persistence through stolen Kerberos tickets. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze ticket lifetimes, authentication patterns, and domain controller logs to determine whether forged or reused tickets are in use",
                    "score": 50
                },
                {
                    "answerText": "Reset user passwords and invalidate sessions to disrupt potential unauthorized access",
                    "score": 32
                },
                {
                    "answerText": "Restart domain controllers and observe whether authentication behavior changes",
                    "score": 18
                },
                {
                    "answerText": "Ignore the suspicion since ticket-based authentication is standard in domain environments",
                    "score": 0
                }
            ],
            "feedback": "Analyzing Kerberos tickets is strongest because persistence may rely on forged tickets. Resetting is containment. Restarting is temporary. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Kerberos ticket persistence suspected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_net_022",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineServer,
            "points": 38,
            "question": "A core network device shows configuration drift that enables unauthorized routing paths. What should you check first?",
            "choices": [
                {
                    "answerText": "Compare current configurations with baseline policies and review change logs to determine how unauthorized routes were introduced",
                    "score": 38
                },
                {
                    "answerText": "Restore the device configuration from backup and monitor whether unauthorized changes reappear",
                    "score": 24
                },
                {
                    "answerText": "Restart the device and observe whether routing behavior returns to normal",
                    "score": 12
                },
                {
                    "answerText": "Ignore the drift since network configurations may change during maintenance operations",
                    "score": 0
                }
            ],
            "feedback": "Comparing configurations is strongest because it identifies unauthorized changes. Restoring is reactive. Restarting is temporary. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Unauthorized routing configuration changes",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_data_023",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineStorage,
            "points": 37,
            "question": "Data classification controls indicate sensitive data is being accessed through an unapproved application. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze application access logs, data handling patterns, and integration points to determine how unauthorized access is occurring",
                    "score": 37
                },
                {
                    "answerText": "Block the application and monitor whether sensitive data access attempts continue",
                    "score": 24
                },
                {
                    "answerText": "Restrict user access temporarily and observe whether data access patterns change",
                    "score": 12
                },
                {
                    "answerText": "Ignore the activity since applications may access data differently depending on configuration",
                    "score": 0
                }
            ],
            "feedback": "Analyzing application access is strongest because it identifies the control failure. Blocking is containment. Restricting is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Unauthorized application accessing sensitive data",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_sec_024",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineCyber,
            "points": 42,
            "question": "Indicators suggest an attacker is clearing event logs to avoid detection. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate remaining logs, system artifacts, and timeline data to reconstruct activity and identify log clearing behavior",
                    "score": 42
                },
                {
                    "answerText": "Restore logging systems and monitor whether logs are cleared again during operation",
                    "score": 26
                },
                {
                    "answerText": "Restart systems and observe whether logging resumes normally",
                    "score": 14
                },
                {
                    "answerText": "Ignore the issue since logs may occasionally rotate or clear automatically",
                    "score": 0
                }
            ],
            "feedback": "Reconstructing logs is strongest because attackers often erase evidence. Restoring is reactive. Restarting is temporary. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Event log clearing detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": False
        },

        {
            "id": "hard_end_025",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 1},
                "medium": {"allowed": True, "weight": 3},
                "hard": {"allowed": True, "weight": 10}
            },
            "location": defineRD,
            "points": 36,
            "question": "Advanced telemetry indicates a rootkit may be present on a critical system. What should you check first?",
            "choices": [
                {
                    "answerText": "Analyze kernel-level behavior, system integrity checks, and low-level system calls to determine whether rootkit activity is present",
                    "score": 36
                },
                {
                    "answerText": "Reimage the system and monitor whether suspicious behavior returns after restoration",
                    "score": 24
                },
                {
                    "answerText": "Run antivirus scans and rely on signature-based detection to identify the threat",
                    "score": 12
                },
                {
                    "answerText": "Ignore the alert since rootkit detections may sometimes be false positives",
                    "score": 0
                }
            ],
            "feedback": "Analyzing kernel behavior is strongest because rootkits operate at a low level. Reimaging is drastic but valid later. Antivirus is limited. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Suspected rootkit on critical system",
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
            "location": defineHelpdesk,
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
            "id": "trap_easy_001",
            "question_difficulty": "Easy",
            "spawn_rules": {
                "easy": {"allowed": True, "weight": 4},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 1}
            },
            "location": defineHelpdesk,
            "points": 7,
            "question": "A user reports receiving a suspicious email from a coworker with an unexpected attachment. What should you do first?",
            "choices": [
                {
                    "answerText": "Verify the message with the coworker through a separate channel and preserve the email for analysis",
                    "score": 7
                },
                {
                    "answerText": "Tell the user to delete the email and avoid opening the attachment without collecting more details",
                    "score": 0
                },
                {
                    "answerText": "Ask the user to open the attachment because it came from an internal sender account",
                    "score": -6
                }
            ],
            "feedback": "The trap is trusting an internal sender without verification. Verifying out-of-band and preserving the email is strongest because internal accounts can be compromised. Deleting the email avoids interaction but removes useful evidence. Opening the attachment makes the situation worse because it may execute malware.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected attachment from internal sender",
            "followup_event": {"allowed": True, "event_id": "trap_easy_001_followup", "score_cutoff": 7},
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
            "location": defineHelpdesk,
            "points": 0,
            "question": "The attachment was opened and the user's system is now acting unusually slow. How do you recover?",
            "choices": [
                {
                    "answerText": "Isolate the workstation from the network and review endpoint activity for signs of malware execution",
                    "score": 0
                },
                {
                    "answerText": "Restart the workstation and ask the user to report if performance problems continue afterward",
                    "score": -3
                },
                {
                    "answerText": "Forward the same attachment to IT staff so they can test it on another workstation",
                    "score": -8
                }
            ],
            "feedback": "Once the attachment has been opened, the best recovery is containment and endpoint review. Restarting may hide symptoms without removing the threat. Forwarding the attachment spreads the risk and repeats the original mistake.",
            "shorthand": "Endpoint Issue",
            "longhand": "Attachment opened before verification",
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
            "location": defineCubicle,
            "points": 6,
            "question": "A user says they found a USB drive in the office and wants to know if they can check what is on it. What should you do first?",
            "choices": [
                {
                    "answerText": "Tell the user not to plug it in and have the device handled through approved security procedures",
                    "score": 6
                },
                {
                    "answerText": "Tell the user to label the device and place it aside until someone can inspect it later",
                    "score": 0
                },
                {
                    "answerText": "Tell the user to plug it into their workstation but avoid opening any unknown files",
                    "score": -5
                }
            ],
            "feedback": "The trap is treating unknown removable media as harmless if files are not opened. The safest answer prevents connection entirely and routes the device through approved handling. Setting it aside avoids immediate execution but does not fully control the device. Plugging it in can trigger malware or device-level attacks.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown USB found in office",
            "followup_event": {"allowed": True, "event_id": "trap_easy_002_followup", "score_cutoff": 6},
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
            "location": defineCubicle,
            "points": 0,
            "question": "The USB device was plugged in and the system now shows an unfamiliar process. How do you recover?",
            "choices": [
                {
                    "answerText": "Disconnect the system from the network and investigate the process, autoruns, and recent device activity",
                    "score": 0
                },
                {
                    "answerText": "End the unfamiliar process and allow the user to continue working while monitoring the system",
                    "score": -3
                },
                {
                    "answerText": "Copy the USB contents to a shared folder so security staff can inspect them remotely",
                    "score": -8
                }
            ],
            "feedback": "The best recovery is containment and investigation because the device may have introduced malware. Ending one process may miss persistence or other activity. Copying the contents to a shared folder risks spreading malicious files.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown USB causes suspicious process",
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
            "location": defineHelpdesk,
            "points": 8,
            "question": "A user reports repeated MFA prompts they did not request. What should you do first?",
            "choices": [
                {
                    "answerText": "Review login attempts, deny active prompts, and secure the account before any prompt is approved",
                    "score": 8
                },
                {
                    "answerText": "Tell the user to ignore the prompts and report back if they continue for several hours",
                    "score": 0
                },
                {
                    "answerText": "Tell the user to approve one prompt to see whether the alerts stop afterward",
                    "score": -7
                }
            ],
            "feedback": "The trap is treating repeated MFA prompts as an annoyance rather than an active login attempt. Reviewing attempts and securing the account is strongest. Ignoring the prompts avoids direct approval but delays response. Approving one prompt may give an attacker access.",
            "shorthand": "Access Issue",
            "longhand": "Unexpected repeated MFA prompts",
            "followup_event": {"allowed": True, "event_id": "trap_easy_003_followup", "score_cutoff": 8},
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
            "location": defineHelpdesk,
            "points": 0,
            "question": "The user approved an MFA prompt and now sees a login from an unfamiliar location. How do you recover?",
            "choices": [
                {
                    "answerText": "Revoke active sessions, reset the password, review login activity, and verify MFA settings",
                    "score": 0
                },
                {
                    "answerText": "Ask the user to watch for more alerts and report if another unfamiliar login appears",
                    "score": -3
                },
                {
                    "answerText": "Disable MFA so the user stops receiving confusing prompts during future sign-ins",
                    "score": -8
                }
            ],
            "feedback": "Once an unauthorized prompt is approved, the best recovery is to revoke sessions and secure the account. Waiting allows the attacker more time. Disabling MFA removes a major protection and makes the compromise worse.",
            "shorthand": "Access Issue",
            "longhand": "MFA approval allowed suspicious login",
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
            "location": defineCopier,
            "points": 5,
            "question": "Sensitive documents are found unattended on a shared printer. What should you do first?",
            "choices": [
                {
                    "answerText": "Secure the documents, identify the owner, and determine whether unauthorized people may have seen them",
                    "score": 5
                },
                {
                    "answerText": "Place the documents beside the printer so the owner can find them when they return",
                    "score": 0
                },
                {
                    "answerText": "Throw the documents away so nobody else can read the sensitive information",
                    "score": -4
                }
            ],
            "feedback": "The trap is treating exposed documents as a simple cleanup issue. Securing them preserves confidentiality and accountability. Leaving them nearby does not make exposure worse immediately but keeps the risk open. Throwing them away may destroy needed information and removes the ability to identify the source.",
            "shorthand": "Data Issue",
            "longhand": "Sensitive documents left at printer",
            "followup_event": {"allowed": True, "event_id": "trap_easy_004_followup", "score_cutoff": 5},
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
            "location": defineCopier,
            "points": 0,
            "question": "The documents were discarded before the owner was identified, and a manager asks what was exposed. How do you recover?",
            "choices": [
                {
                    "answerText": "Document what is known, check print logs, and identify the likely owner and document source",
                    "score": 0
                },
                {
                    "answerText": "Ask nearby employees if they remember seeing the documents before they were discarded",
                    "score": -2
                },
                {
                    "answerText": "Report that there is no issue because the documents are no longer visible",
                    "score": -6
                }
            ],
            "feedback": "The best recovery is to reconstruct the exposure using logs and known details. Asking around may help but spreads awareness of the incident and may be incomplete. Claiming there is no issue ignores that exposure may already have occurred.",
            "shorthand": "Data Issue",
            "longhand": "Discarded sensitive documents before review",
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
            "location": defineCubicle,
            "points": 9,
            "question": "A user reports that their browser redirects searches to unfamiliar websites. What should you do first?",
            "choices": [
                {
                    "answerText": "Check browser extensions, DNS settings, and recent changes for signs of hijacking or unwanted software",
                    "score": 9
                },
                {
                    "answerText": "Reset the homepage and default search engine, then monitor whether the redirects continue",
                    "score": 0
                },
                {
                    "answerText": "Tell the user to keep using the browser because redirects are common advertising behavior",
                    "score": -6
                }
            ],
            "feedback": "The trap is treating redirects as a browser preference issue instead of a possible compromise. Checking extensions, DNS, and recent changes targets the likely cause. Resetting settings may hide the symptom but does not confirm source. Continuing to browse increases exposure.",
            "shorthand": "Network Issue",
            "longhand": "Browser redirects to unfamiliar websites",
            "followup_event": {"allowed": True, "event_id": "trap_easy_005_followup", "score_cutoff": 9},
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
            "location": defineCubicle,
            "points": 0,
            "question": "The redirects continued and the user entered credentials on one of the unfamiliar sites. How do you recover?",
            "choices": [
                {
                    "answerText": "Reset the affected credentials, review login activity, and investigate the workstation for browser or DNS compromise",
                    "score": 0
                },
                {
                    "answerText": "Clear the browser history and ask the user to avoid using unfamiliar websites going forward",
                    "score": -3
                },
                {
                    "answerText": "Tell the user to retry the login on the same site to confirm whether the password works",
                    "score": -8
                }
            ],
            "feedback": "The best recovery is to treat the credentials as exposed and investigate the redirect cause. Clearing history removes local evidence and does not secure the account. Retrying the login gives the suspicious site another chance to capture credentials.",
            "shorthand": "Access Issue",
            "longhand": "Credentials entered after browser redirect",
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
            "location": defineCyber,
            "points": 22,
            "question": "Multiple users report receiving similar phishing emails that appear to come from an internal department account. What should you do first?",
            "choices": [
                {
                    "answerText": "Preserve samples, analyze headers, verify the sender account status, and determine whether the internal account is compromised",
                    "score": 22
                },
                {
                    "answerText": "Tell users to delete the emails and avoid clicking links while waiting to see if more reports arrive",
                    "score": 0
                },
                {
                    "answerText": "Trust the messages because they came from an internal account and ask users to follow the instructions carefully",
                    "score": -14
                }
            ],
            "feedback": "The trap is assuming internal email is safe. Preserving and analyzing the messages is strongest because internal accounts can be compromised and used for phishing. Deleting the emails avoids some immediate interaction but loses evidence and delays containment. Trusting the message makes the incident worse by helping the attacker reach more users.",
            "shorthand": "Security Issue",
            "longhand": "Internal account sending phishing emails",
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
            "location": defineCyber,
            "points": 0,
            "question": "The internal sender account was trusted, and several users entered credentials through the linked page. How do you recover?",
            "choices": [
                {
                    "answerText": "Reset exposed credentials, revoke sessions, review login activity, and contain the compromised internal sender account",
                    "score": 0
                },
                {
                    "answerText": "Send a reminder telling users not to click future links while waiting for more suspicious activity",
                    "score": -8
                },
                {
                    "answerText": "Delete the reported emails from mailboxes without reviewing which users submitted credentials",
                    "score": -18
                }
            ],
            "feedback": "The best recovery is to secure affected accounts and contain the compromised sender because credentials were exposed. Sending a reminder may reduce future clicks but does not address active compromise. Deleting emails without identifying victims removes evidence and leaves compromised accounts active.",
            "shorthand": "Access Issue",
            "longhand": "Users submitted credentials through internal phishing",
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
            "location": defineServer,
            "points": 20,
            "question": "Network monitoring shows high outbound traffic from a single workstation to an unfamiliar external address. What should you do first?",
            "choices": [
                {
                    "answerText": "Identify the process generating traffic, review destination reputation, and determine whether the activity indicates data exfiltration",
                    "score": 20
                },
                {
                    "answerText": "Restart the workstation and monitor whether outbound traffic returns to normal after the reboot",
                    "score": 0
                },
                {
                    "answerText": "Ignore the traffic spike because workstations may upload large files during normal business activity",
                    "score": -12
                }
            ],
            "feedback": "The trap is treating a traffic spike as normal without validating the source. Checking process, destination, and exfiltration indicators is strongest. Restarting may stop symptoms but can lose volatile evidence and skip root cause. Ignoring the spike can allow data theft to continue.",
            "shorthand": "Network Issue",
            "longhand": "Workstation sending unusual outbound traffic",
            "followup_event": {"allowed": True, "event_id": "trap_medium_002_followup", "score_cutoff": 20},
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
            "location": defineServer,
            "points": 0,
            "question": "The workstation was restarted before analysis, but outbound traffic resumed after login. How do you recover?",
            "choices": [
                {
                    "answerText": "Isolate the workstation, capture current traffic details, and review process activity before taking further remediation steps",
                    "score": 0
                },
                {
                    "answerText": "Restart the workstation again and wait longer before allowing the user to sign back in",
                    "score": -7
                },
                {
                    "answerText": "Allow the user to continue working because the reboot did not permanently damage the system",
                    "score": -16
                }
            ],
            "feedback": "The best recovery is to isolate and analyze the active behavior now that the symptom returned. Restarting again repeats the same mistake and may continue losing evidence. Allowing normal work gives the suspicious process more time to communicate externally.",
            "shorthand": "Network Issue",
            "longhand": "Outbound traffic resumes after premature reboot",
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
            "location": defineStorage,
            "points": 24,
            "question": "Audit logs show a user downloading many sensitive files shortly before leaving the company. What should you do first?",
            "choices": [
                {
                    "answerText": "Review access patterns, confirm business justification, preserve logs, and assess whether the downloads indicate data theft",
                    "score": 24
                },
                {
                    "answerText": "Ask the user directly whether they needed the files and continue monitoring if they say it was legitimate",
                    "score": 0
                },
                {
                    "answerText": "Delete the user's downloaded copies remotely without preserving logs or reviewing the scope of access",
                    "score": -15
                }
            ],
            "feedback": "The trap is resolving a data-risk event through a casual user explanation. Reviewing patterns and preserving logs is strongest because insider data theft requires evidence and scope. Asking the user alone may alert them and does not verify activity. Deleting copies without preserving evidence can damage the investigation.",
            "shorthand": "Data Issue",
            "longhand": "Departing user downloads sensitive files",
            "followup_event": {"allowed": True, "event_id": "trap_medium_003_followup", "score_cutoff": 24},
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
            "location": defineStorage,
            "points": 0,
            "question": "The user was questioned first, and file activity stopped before logs were preserved. How do you recover?",
            "choices": [
                {
                    "answerText": "Preserve remaining logs, review access history, and coordinate with management to assess exposure and response requirements",
                    "score": 0
                },
                {
                    "answerText": "Wait to see if the user downloads more files before escalating the situation further",
                    "score": -8
                },
                {
                    "answerText": "Delete the user's account immediately without reviewing what data may already have been copied",
                    "score": -18
                }
            ],
            "feedback": "The best recovery is to preserve remaining evidence and assess exposure even if the user has been alerted. Waiting risks losing more evidence. Deleting the account may stop future access but does not determine what was already taken.",
            "shorthand": "Data Issue",
            "longhand": "Insider download activity disrupted before preservation",
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
            "location": defineCubicle,
            "points": 18,
            "question": "An endpoint alert shows an unknown scheduled task running under a normal user account. What should you do first?",
            "choices": [
                {
                    "answerText": "Review the scheduled task details, associated executable, and recent system activity to determine whether it is persistence",
                    "score": 18
                },
                {
                    "answerText": "Disable the task and allow the user to continue working while watching for another alert",
                    "score": 0
                },
                {
                    "answerText": "Whitelist the task because it is running under a normal user account instead of an administrator account",
                    "score": -12
                }
            ],
            "feedback": "The trap is assuming normal-user context means low risk. Reviewing the task and executable is strongest because scheduled tasks are common persistence mechanisms. Disabling the task without analysis may hide useful evidence. Whitelisting it makes the environment trust potentially malicious persistence.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown scheduled task under user account",
            "followup_event": {"allowed": True, "event_id": "trap_medium_004_followup", "score_cutoff": 18},
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
            "location": defineCubicle,
            "points": 0,
            "question": "The task was disabled without analysis, but a similar task appeared later under a different name. How do you recover?",
            "choices": [
                {
                    "answerText": "Isolate the endpoint and investigate task creation events, related executables, and parent process activity",
                    "score": 0
                },
                {
                    "answerText": "Disable the new task and continue repeating that process if it appears again",
                    "score": -7
                },
                {
                    "answerText": "Whitelist the new task name so repeated alerts stop interrupting the user",
                    "score": -16
                }
            ],
            "feedback": "The best recovery is to investigate how the tasks are being created because recurrence indicates persistence. Repeatedly disabling tasks treats symptoms only. Whitelisting suppresses the warning and lets the attacker maintain a foothold.",
            "shorthand": "Endpoint Issue",
            "longhand": "Scheduled task persistence returns after removal",
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
            "location": defineCyber,
            "points": 26,
            "question": "A privileged account shows a successful login shortly after many failed attempts from the same source. What should you do first?",
            "choices": [
                {
                    "answerText": "Correlate failed and successful authentication events, verify source details, and determine whether the login was unauthorized",
                    "score": 26
                },
                {
                    "answerText": "Reset the account password and watch for additional failed login attempts from the same source",
                    "score": 0
                },
                {
                    "answerText": "Assume the user eventually remembered the correct password and close the alert as normal behavior",
                    "score": -16
                }
            ],
            "feedback": "The trap is treating failed attempts followed by success as normal user behavior. Correlating the authentication chain is strongest because it may reveal a successful brute-force or password spray attempt. Resetting the password helps but skips scope analysis. Closing the alert ignores a serious compromise pattern.",
            "shorthand": "Access Issue",
            "longhand": "Failed logins followed by privileged success",
            "followup_event": {"allowed": True, "event_id": "trap_medium_005_followup", "score_cutoff": 26},
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
            "location": defineCyber,
            "points": 0,
            "question": "The password was reset, but the account had already accessed several sensitive systems. How do you recover?",
            "choices": [
                {
                    "answerText": "Review session activity, revoke active tokens, check accessed systems, and determine what actions occurred after login",
                    "score": 0
                },
                {
                    "answerText": "Assume the password reset resolved the issue and continue monitoring for future login failures",
                    "score": -8
                },
                {
                    "answerText": "Delete authentication logs to reduce confusion and avoid duplicate investigation of the same account",
                    "score": -20
                }
            ],
            "feedback": "The best recovery is to review post-login activity because the attacker may have already acted. Assuming the reset solved everything ignores actions taken before containment. Deleting logs destroys evidence and severely worsens the response.",
            "shorthand": "Access Issue",
            "longhand": "Privileged account used before containment",
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
            "location": defineCyber,
            "points": 46,
            "question": "Logs indicate possible lateral movement using valid admin credentials across multiple servers. What should you do first?",
            "choices": [
                {
                    "answerText": "Correlate authentication paths, session usage, and host activity to determine how credentials are being used across systems",
                    "score": 46
                },
                {
                    "answerText": "Reset the administrator password and monitor whether further lateral movement attempts appear in logs",
                    "score": 0
                },
                {
                    "answerText": "Assume this is normal administrative behavior since admins frequently access multiple systems",
                    "score": -20
                }
            ],
            "feedback": "The trap is assuming valid credentials mean legitimate activity. Correlating movement paths is strongest because it identifies attacker behavior. Resetting helps containment but ignores scope. Assuming legitimacy allows the attacker to continue moving freely.",
            "shorthand": "Security Issue",
            "longhand": "Lateral movement using valid admin credentials",
            "followup_event": {"allowed": True, "event_id": "trap_hard_001_followup", "score_cutoff": 46},
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
            "location": defineCyber,
            "points": 0,
            "question": "The password was reset, but logs show continued movement using existing sessions. How do you recover?",
            "choices": [
                {
                    "answerText": "Revoke active sessions, review token usage, and trace prior system access to determine persistence mechanisms",
                    "score": 0
                },
                {
                    "answerText": "Reset the password again and monitor whether the activity stops after the second reset",
                    "score": -8
                },
                {
                    "answerText": "Ignore session activity since password resets should prevent future unauthorized access",
                    "score": -22
                }
            ],
            "feedback": "The best recovery is session revocation and investigation because attackers may maintain access through tokens. Resetting again repeats the mistake. Ignoring session activity allows persistence to continue.",
            "shorthand": "Access Issue",
            "longhand": "Active sessions persist after password reset",
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
            "location": defineServer,
            "points": 44,
            "question": "A critical server shows sustained encrypted outbound traffic to unknown destinations. What should you do first?",
            "choices": [
                {
                    "answerText": "Analyze traffic patterns, process origins, and destination reputation to determine whether the activity represents data exfiltration",
                    "score": 44
                },
                {
                    "answerText": "Block all outbound traffic from the server and monitor whether operations are impacted",
                    "score": 0
                },
                {
                    "answerText": "Ignore the traffic because encryption is commonly used for secure communications",
                    "score": -18
                }
            ],
            "feedback": "The trap is assuming encrypted traffic is inherently safe. Analyzing the traffic is strongest because it identifies exfiltration. Blocking traffic helps containment but skips investigation. Ignoring the behavior allows potential data loss.",
            "shorthand": "Network Issue",
            "longhand": "Encrypted outbound traffic from critical server",
            "followup_event": {"allowed": True, "event_id": "trap_hard_002_followup", "score_cutoff": 44},
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
            "location": defineServer,
            "points": 0,
            "question": "Outbound traffic was blocked, but logs show large transfers occurred before containment. How do you recover?",
            "choices": [
                {
                    "answerText": "Review transfer logs, identify exposed data, and determine the scope and destination of the exfiltration",
                    "score": 0
                },
                {
                    "answerText": "Keep traffic blocked and assume the issue is fully resolved without further investigation",
                    "score": -10
                },
                {
                    "answerText": "Restore server connectivity and test whether transfers continue under normal conditions",
                    "score": -20
                }
            ],
            "feedback": "The best recovery is to assess what data was exposed before containment. Assuming resolution ignores damage already done. Restoring connectivity without analysis risks continued exfiltration.",
            "shorthand": "Data Issue",
            "longhand": "Data exfiltration occurred before containment",
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
            "location": defineRD,
            "points": 48,
            "question": "Endpoint telemetry shows fileless malware activity with no disk artifacts present. What should you do first?",
            "choices": [
                {
                    "answerText": "Analyze memory, process injection behavior, and runtime execution patterns to identify how the malware is operating",
                    "score": 48
                },
                {
                    "answerText": "Restart the system and monitor whether the suspicious behavior reappears after reboot",
                    "score": 0
                },
                {
                    "answerText": "Ignore the alert because no files are present on disk to indicate a persistent threat",
                    "score": -22
                }
            ],
            "feedback": "The trap is relying on disk artifacts to confirm compromise. Memory analysis is strongest because fileless malware resides in memory. Restarting removes evidence temporarily. Ignoring allows the threat to persist undetected.",
            "shorthand": "Endpoint Issue",
            "longhand": "Fileless malware with no disk artifacts",
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
            "location": defineRD,
            "points": 0,
            "question": "The system was restarted and the activity stopped temporarily, but later returned. How do you recover?",
            "choices": [
                {
                    "answerText": "Perform memory and behavioral analysis while the system is active to identify persistence and propagation mechanisms",
                    "score": 0
                },
                {
                    "answerText": "Restart the system again and wait longer before allowing users to log back in",
                    "score": -9
                },
                {
                    "answerText": "Assume the issue resolved temporarily and allow normal operations without further investigation",
                    "score": -20
                }
            ],
            "feedback": "The best recovery is to analyze the active state because rebooting removed evidence. Repeating reboots delays detection. Ignoring allows persistent threats to continue operating.",
            "shorthand": "Endpoint Issue",
            "longhand": "Fileless malware returns after reboot",
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
            "location": defineStorage,
            "points": 43,
            "question": "Database logs show subtle, continuous extraction of small amounts of sensitive data over time. What should you do first?",
            "choices": [
                {
                    "answerText": "Analyze query patterns, user activity, and timing to determine whether the behavior represents stealthy data exfiltration",
                    "score": 43
                },
                {
                    "answerText": "Restrict database access temporarily and observe whether extraction behavior stops",
                    "score": 0
                },
                {
                    "answerText": "Ignore the activity because small data transfers are common in normal database usage",
                    "score": -17
                }
            ],
            "feedback": "The trap is assuming small transfers are harmless. Analyzing patterns is strongest because stealth exfiltration is gradual. Restricting access helps containment but misses analysis. Ignoring allows long-term data loss.",
            "shorthand": "Data Issue",
            "longhand": "Stealthy gradual data extraction detected",
            "followup_event": {"allowed": True, "event_id": "trap_hard_004_followup", "score_cutoff": 43},
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
            "location": defineStorage,
            "points": 0,
            "question": "Access was restricted, but logs show the attacker extracted data over several days before detection. How do you recover?",
            "choices": [
                {
                    "answerText": "Determine the scope of exposed data, review access logs, and begin incident response procedures for potential data breach",
                    "score": 0
                },
                {
                    "answerText": "Restore database permissions and assume the restriction solved the issue going forward",
                    "score": -10
                },
                {
                    "answerText": "Delete database logs to simplify the environment and avoid further confusion",
                    "score": -25
                }
            ],
            "feedback": "The best recovery is to assess breach impact and respond accordingly. Restoring permissions without analysis ignores damage. Deleting logs destroys critical evidence.",
            "shorthand": "Data Issue",
            "longhand": "Confirmed data exfiltration before restriction",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        },

        {
            "id": "trap_hard_005",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 2},
                "hard": {"allowed": True, "weight": 4}
            },
            "location": defineCyber,
            "points": 50,
            "question": "Logs indicate that security logging services are being disabled across multiple systems. What should you do first?",
            "choices": [
                {
                    "answerText": "Investigate how logging is being disabled, review privilege usage, and determine whether attackers are attempting to evade detection",
                    "score": 50
                },
                {
                    "answerText": "Re-enable logging services and monitor whether they are disabled again during system operation",
                    "score": 0
                },
                {
                    "answerText": "Ignore the issue because logging services may restart or stop during updates",
                    "score": -20
                }
            ],
            "feedback": "The trap is treating logging failures as routine behavior. Investigating cause is strongest because attackers disable logs to hide activity. Re-enabling is reactive and may not persist. Ignoring removes visibility entirely.",
            "shorthand": "Security Issue",
            "longhand": "Logging services disabled across systems",
            "followup_event": {"allowed": True, "event_id": "trap_hard_005_followup", "score_cutoff": 50},
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
            "location": defineCyber,
            "points": 0,
            "question": "Logging was restored, but gaps exist during the period it was disabled. How do you recover?",
            "choices": [
                {
                    "answerText": "Reconstruct activity using remaining logs, correlate system behavior, and identify actions taken during the logging gap",
                    "score": 0
                },
                {
                    "answerText": "Assume no critical activity occurred during the gap and continue monitoring going forward",
                    "score": -12
                },
                {
                    "answerText": "Clear remaining logs and restart logging to create a clean baseline environment",
                    "score": -28
                }
            ],
            "feedback": "The best recovery is reconstruction using available data because attackers may have acted during the gap. Assuming no activity ignores risk. Clearing logs destroys remaining evidence.",
            "shorthand": "Security Issue",
            "longhand": "Log gap after logging disruption",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        }
    ]
    return
