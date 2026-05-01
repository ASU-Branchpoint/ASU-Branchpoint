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
            "question": "A user reports a pop-up claiming their computer is infected and instructing them to call a support number. What steps should you take?",
            "choices": [
                {
                    "answerText": "Have the user stop interacting with the pop-up, isolate the system if needed, and verify whether the alert originated from approved security software",
                    "score": 5
                },
                {
                    "answerText": "Ask the user to close the browser, capture a screenshot for documentation, and continue working while monitoring for any additional unusual behavior",
                    "score": 3
                },
                {
                    "answerText": "Call the number shown in the alert to confirm legitimacy, provide details if requested, and follow any instructions given by the supposed support contact",
                    "score": 0
                }
            ],
            "feedback": "Stopping interaction and verifying the alert source is strongest because these pop-ups are commonly used for scams. Closing the browser and monitoring is reasonable but does not confirm whether anything executed. Calling the number is the weakest option because it directly engages with a likely attacker.",
            "shorthand": "Security Issue",
            "longhand": "Fake malware pop-up requests user action",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Review authentication logs for failed attempts and identify whether another system, service, or process is repeatedly using outdated or incorrect credentials",
                    "score": 8
                },
                {
                    "answerText": "Unlock the account and allow the user to attempt logging in again while observing whether the lockout condition reoccurs during normal activity",
                    "score": 5
                },
                {
                    "answerText": "Disable the account temporarily to prevent further access attempts, without first determining the cause of the lockout or reviewing recent authentication activity",
                    "score": 1
                }
            ],
            "feedback": "Reviewing logs is strongest because unexpected lockouts often indicate password attacks or misconfigured services. Unlocking and observing is reactive. Disabling the account without investigation disrupts access without identifying cause.",
            "shorthand": "Access Issue",
            "longhand": "Unexpected account lockout activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user reports receiving an email asking them to verify their login credentials through a link. What steps should you take?",
            "choices": [
                {
                    "answerText": "Examine the email headers and inspect the link destination carefully to determine whether the message is a phishing attempt before taking further action",
                    "score": 6
                },
                {
                    "answerText": "Ask the user to delete the email immediately, avoid interacting with it, and continue working without performing additional analysis or verification",
                    "score": 3
                },
                {
                    "answerText": "Click the link in a controlled browser session to see whether the login page appears legitimate and matches the expected service interface",
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
            "question": "A user plugs in an unknown USB device they found in the office. What steps should you take?",
            "choices": [
                {
                    "answerText": "Disconnect the USB device immediately and check the system for unauthorized processes, suspicious activity, or indicators of malicious execution",
                    "score": 7
                },
                {
                    "answerText": "Leave the device connected temporarily and monitor the system over time to see if any unusual behavior or performance issues become apparent",
                    "score": 3
                },
                {
                    "answerText": "Open the device contents and copy files locally to inspect them more closely for anything suspicious or out of place within the file structure",
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
            "question": "A user reports receiving multiple login alerts from different geographic locations within a short period. What steps should you take?",
            "choices": [
                {
                    "answerText": "Review authentication logs, secure the account with a password reset, and verify whether multi-factor authentication is properly enabled and functioning",
                    "score": 9
                },
                {
                    "answerText": "Ask the user whether they were traveling, using a VPN, or accessing services remotely in a way that might explain the unusual login locations",
                    "score": 4
                },
                {
                    "answerText": "Assume the alerts are inaccurate location reports and take no immediate action, since some services may misidentify login origins under normal conditions",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs and securing the account is strongest because this pattern indicates compromise risk. Asking the user is useful but secondary. Ignoring alerts is weakest because it dismisses a clear warning sign.",
            "shorthand": "Access Issue",
            "longhand": "Multiple suspicious login alerts detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user clicked a suspicious link in an email but reports nothing happened. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check the system for indicators of compromise and review logs to determine whether any background activity or malicious execution was triggered",
                    "score": 7
                },
                {
                    "answerText": "Restart the system and observe whether any unusual behavior appears during normal use, noting performance or application irregularities",
                    "score": 3
                },
                {
                    "answerText": "Assume no action is necessary since the user did not observe visible changes, and continue normal operations without further investigation",
                    "score": 0
                }
            ],
            "feedback": "Checking for indicators of compromise is strongest because attacks may not show immediate signs. Restarting is less targeted but may reveal instability. Assuming nothing happened is weakest because it ignores potential silent compromise.",
            "shorthand": "Security Issue",
            "longhand": "User clicked phishing link",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user installs software from an unverified website without approval. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check the system for indicators of compromise and review logs to determine whether any background activity or malicious execution was triggered",
                    "score": 7
                },
                {
                    "answerText": "Restart the system and observe whether any unusual behavior appears during normal use, noting performance or application irregularities",
                    "score": 3
                },
                {
                    "answerText": "Assume no action is necessary since the user did not observe visible changes, and continue normal operations without further investigation",
                    "score": 0
                }
            ],
            "feedback": "Verifying and removing unauthorized software is strongest because it may introduce risk. Monitoring without validation is weaker. Deploying it elsewhere is the worst option because it spreads potential compromise.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unauthorized software installed on system",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "Sensitive documents are found left unattended at a shared printer. What steps should you take?",
            "choices": [
                {
                    "answerText": "Secure the documents immediately, identify the owner, and review whether any unauthorized individuals may have accessed the information",
                    "score": 4
                },
                {
                    "answerText": "Leave the documents in place and wait for the original user to return, assuming they will retrieve them without intervention",
                    "score": 2
                },
                {
                    "answerText": "Discard the documents without verifying their contents or importance, and do not attempt to identify the responsible individual",
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
            "question": "A user shares their password with a coworker to complete a task more quickly. What steps should you take?",
            "choices": [
                {
                    "answerText": "Instruct the user to change their password immediately and reinforce policies regarding credential sharing and proper account security practices",
                    "score": 5
                },
                {
                    "answerText": "Allow the behavior temporarily due to urgency, assuming the shared credentials were only used for a short period to complete a task",
                    "score": 2
                },
                {
                    "answerText": "Ignore the situation since both users are trusted employees within the same department and likely have legitimate intentions",
                    "score": 0
                }
            ],
            "feedback": "Resetting the password and reinforcing policy is strongest because credential sharing is a violation. Allowing it weakens controls. Ignoring it normalizes insecure behavior.",
            "shorthand": "Access Issue",
            "longhand": "User shares credentials with coworker",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user reports receiving an unexpected file attachment from an internal coworker. What steps should you take?",
            "choices": [
                {
                    "answerText": "Verify the sender through a separate communication channel and analyze the attachment carefully before allowing it to be opened",
                    "score": 8
                },
                {
                    "answerText": "Open the attachment within a sandboxed or isolated environment to observe behavior and determine whether any malicious activity occurs",
                    "score": 4
                },
                {
                    "answerText": "Assume the file is safe because it came from an internal account and allow the user to proceed without additional verification",
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
            "question": "A user notices their browser homepage has changed without their input. What steps should you take?",
            "choices": [
                {
                    "answerText": "Review browser extensions, recent installations, and system changes to determine whether unauthorized modifications were introduced",
                    "score": 6
                },
                {
                    "answerText": "Reset the homepage manually and continue working while monitoring the system for any additional unexpected changes over time",
                    "score": 3
                },
                {
                    "answerText": "Ignore the change since browser updates may adjust settings automatically during normal operation without user input",
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
            "question": "A user reports their account sent emails they did not write. What steps should you take?",
            "choices": [
                {
                    "answerText": "Secure the account by resetting the password, reviewing sent messages, and checking logs for unauthorized login activity",
                    "score": 10
                },
                {
                    "answerText": "Ask the user to monitor their account activity and report if additional unauthorized emails are sent in the future",
                    "score": 4
                },
                {
                    "answerText": "Assume the emails were delayed or cached messages and continue normal operations without investigating the reported behavior",
                    "score": 0
                }
            ],
            "feedback": "Securing the account is strongest because this indicates likely compromise. Monitoring is reactive and delays response. Ignoring it is weakest because it dismisses a critical indicator.",
            "shorthand": "Security Issue",
            "longhand": "Account sending unauthorized emails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user notices a program installed on their system that they do not recognize. What steps should you take?",
            "choices": [
                {
                    "answerText": "Identify the program, verify its legitimacy, and review system activity to determine whether it was installed maliciously",
                    "score": 7
                },
                {
                    "answerText": "Leave the program installed and monitor system performance over time to see whether any issues or anomalies develop",
                    "score": 3
                },
                {
                    "answerText": "Ignore the program since system updates may install additional components automatically without user awareness or notification",
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
            "question": "A user receives repeated password reset emails they did not request. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check account activity, reset the password, and verify whether repeated unauthorized password reset attempts are being made",
                    "score": 6
                },
                {
                    "answerText": "Ask the user to ignore the emails unless they notice any direct changes to their account or access behavior",
                    "score": 2
                },
                {
                    "answerText": "Disable password reset functionality temporarily to stop notifications without investigating the underlying cause",
                    "score": 0
                }
            ],
            "feedback": "Checking activity and securing the account is strongest because reset attempts may indicate targeting. Ignoring is weaker and reactive. Disabling resets is weakest because it breaks functionality without solving the issue.",
            "shorthand": "Access Issue",
            "longhand": "Unrequested password reset emails",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user reports their system camera activated briefly without their input. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check running processes, application permissions, and logs to determine whether unauthorized access to the camera occurred",
                    "score": 9
                },
                {
                    "answerText": "Restart the system and observe whether the issue occurs again during normal use or application activity",
                    "score": 3
                },
                {
                    "answerText": "Assume the behavior is normal since applications may briefly access hardware devices during updates or initialization",
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
                    "answerText": "Check DNS settings, browser configuration, and network behavior to determine whether a redirect or hijacking condition exists",
                    "score": 8
                },
                {
                    "answerText": "Ask the user to continue browsing normally and report whether the redirects become more frequent or consistent over time",
                    "score": 2
                },
                {
                    "answerText": "Ignore the issue since some websites may redirect users depending on region, content, or load balancing conditions",
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
                    "answerText": "Reset the password immediately and allow the user to regain access without checking for recent activity or anomalies",
                    "score": 4
                },
                {
                    "answerText": "Assume the user entered the password incorrectly and instruct them to retry multiple times before taking further action",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because unexpected failure may indicate compromise. Resetting is reactive. Assuming user error is weakest because it ignores risk.",
            "shorthand": "Access Issue",
            "longhand": "Password unexpectedly invalid",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Restore the document from backup and continue working without identifying the source or cause of the modification",
                    "score": 3
                },
                {
                    "answerText": "Ignore the issue since version changes may occur automatically in shared environments without direct user input",
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
            "question": "A user receives a phone call asking for login credentials from someone claiming to be IT. What steps should you take?",
            "choices": [
                {
                    "answerText": "Instruct the user not to share credentials, report the incident, and confirm whether any information was already disclosed",
                    "score": 5
                },
                {
                    "answerText": "Advise the user to ignore the call and continue working without reporting the incident or documenting the interaction",
                    "score": 2
                },
                {
                    "answerText": "Ask the user to call the number back to verify legitimacy and provide information if the request appears reasonable",
                    "score": 0
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
            "question": "A user reports frequent pop-up advertisements appearing on their system during normal use. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check for adware by reviewing installed applications, extensions, and recent downloads that may have introduced unwanted software",
                    "score": 6
                },
                {
                    "answerText": "Close the pop-ups and continue working while monitoring whether the issue persists or worsens over time",
                    "score": 2
                },
                {
                    "answerText": "Ignore the behavior since advertisements may appear during normal browsing activity depending on visited websites",
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
            "question": "A removable storage device containing company data is reported missing. What steps should you take?",
            "choices": [
                {
                    "answerText": "Report the incident, determine what data was on the device, and assess whether sensitive information may have been exposed",
                    "score": 8
                },
                {
                    "answerText": "Wait to see if the device is returned before taking further action or escalating the situation to appropriate teams",
                    "score": 2
                },
                {
                    "answerText": "Ignore the situation since removable devices are often misplaced temporarily and may be returned without issue",
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
            "question": "A user notices their microphone is being accessed without their interaction. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check active processes, permissions, and logs to determine whether any unauthorized application accessed the microphone",
                    "score": 9
                },
                {
                    "answerText": "Restart the system and monitor whether the issue occurs again during normal usage or application activity",
                    "score": 3
                },
                {
                    "answerText": "Ignore the behavior since applications may briefly access hardware devices during updates or initialization processes",
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
            "question": "A user entered their credentials into a suspicious website. What steps should you take?",
            "choices": [
                {
                    "answerText": "Immediately reset the password, review account activity, and enforce additional protections such as multi-factor authentication",
                    "score": 10
                },
                {
                    "answerText": "Ask the user to monitor their account for suspicious activity and report any unusual behavior that occurs",
                    "score": 3
                },
                {
                    "answerText": "Ignore the situation since the user recognized the mistake quickly and no visible issues have been reported",
                    "score": 0
                }
            ],
            "feedback": "Resetting credentials is strongest because they may already be compromised. Monitoring is reactive. Ignoring is weakest.",
            "shorthand": "Access Issue",
            "longhand": "Credentials entered into phishing site",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
            "question": "A user notices an unknown browser extension installed without their knowledge. What steps should you take?",
            "choices": [
                {
                    "answerText": "Identify the extension, verify its origin, and remove it while checking for any related unauthorized changes or activity",
                    "score": 7
                },
                {
                    "answerText": "Disable the extension temporarily and continue working while observing system behavior for any noticeable issues",
                    "score": 3
                },
                {
                    "answerText": "Ignore the extension since browsers may install additional components automatically during updates or feature changes",
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
                    "answerText": "Ask the user to delete the emails and monitor whether the volume decreases or changes over time",
                    "score": 3
                },
                {
                    "answerText": "Disable spam filtering temporarily to test whether the system is misclassifying messages or behaving incorrectly",
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
            "location":  defineCyber,
            "points": 22,
            "question": "Multiple users report receiving similar phishing emails that bypassed spam filters. What should you check first?",
            "choices": [
                {
                    "answerText": "Review email filtering rules, analyze message headers, and determine how the phishing campaign bypassed existing detection controls",
                    "score": 22
                },
                {
                    "answerText": "Instruct users to delete the emails, report additional messages, and monitor whether the phishing campaign continues over time",
                    "score": 10
                },
                {
                    "answerText": "Block the sender domain immediately and monitor for additional attempts without reviewing how the messages avoided detection",
                    "score": 4
                },
                {
                    "answerText": "Assume occasional phishing bypass is normal behavior and continue monitoring without performing additional analysis",
                    "score": 0
                }
            ],
            "feedback": "Analyzing filtering and headers is strongest because it identifies why controls failed. Deleting emails is reactive. Blocking domains helps but skips root cause. Ignoring it is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Phishing campaign bypasses email filtering",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
        },

        {
            "id": "medium_acc_002",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location":  defineCyber,
            "points": 24,
            "question": "Authentication logs show repeated successful logins from an unfamiliar IP address for a single user. What should you check first?",
            "choices": [
                {
                    "answerText": "Investigate login patterns, correlate activity with user behavior, and determine whether credentials were compromised",
                    "score": 24
                },
                {
                    "answerText": "Ask the user whether they traveled or used a VPN that could explain the unfamiliar login source",
                    "score": 14
                },
                {
                    "answerText": "Reset the password immediately and monitor for further activity without reviewing historical login patterns",
                    "score": 6
                },
                {
                    "answerText": "Assume IP changes are normal and continue monitoring without investigating the login source",
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
                    "answerText": "Review internal routing, DNS resolution, and service availability to identify inconsistencies affecting internal systems",
                    "score": 21
                },
                {
                    "answerText": "Restart affected systems and monitor whether access stabilizes during normal operation",
                    "score": 9
                },
                {
                    "answerText": "Ask users to retry access and report whether issues persist across multiple attempts",
                    "score": 5
                },
                {
                    "answerText": "Assume the issue is temporary and continue monitoring without further investigation",
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
                    "answerText": "Analyze process activity, review execution history, and determine whether behavior aligns with known malicious patterns",
                    "score": 26
                },
                {
                    "answerText": "Restart the workstation and observe whether the alert appears again during normal usage",
                    "score": 11
                },
                {
                    "answerText": "Isolate the system temporarily and monitor whether unusual behavior continues during operation",
                    "score": 6
                },
                {
                    "answerText": "Disable the alert and assume the behavior is a false positive without further analysis",
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
                    "answerText": "Review access patterns, compare activity with job roles, and assess whether the downloads indicate potential data exfiltration",
                    "score": 23
                },
                {
                    "answerText": "Ask the user about the downloads and monitor for additional activity over time",
                    "score": 12
                },
                {
                    "answerText": "Restrict access temporarily and observe whether similar activity occurs again",
                    "score": 6
                },
                {
                    "answerText": "Assume bulk downloads are normal and continue monitoring without further review",
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
                    "answerText": "Review authentication logs, verify login attempts, and determine whether the account is being targeted",
                    "score": 18
                },
                {
                    "answerText": "Ask the user to ignore prompts and report if the behavior continues over time",
                    "score": 7
                },
                {
                    "answerText": "Reset the password and monitor whether prompts stop without reviewing login activity",
                    "score": 4
                },
                {
                    "answerText": "Disable MFA temporarily to prevent prompts without investigating the cause",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because MFA prompts indicate active login attempts. Ignoring is weaker. Disabling MFA is worst.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected MFA prompt activity",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Analyze traffic destination, volume, and originating process to determine whether data exfiltration is occurring",
                    "score": 20
                },
                {
                    "answerText": "Restart the host and monitor whether outbound traffic returns to expected levels",
                    "score": 8
                },
                {
                    "answerText": "Limit network access temporarily and observe whether traffic patterns change",
                    "score": 5
                },
                {
                    "answerText": "Assume traffic spikes are normal and continue monitoring without investigation",
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
                    "answerText": "Review access control changes, group memberships, and permission updates to determine how access was granted",
                    "score": 19
                },
                {
                    "answerText": "Remove the access immediately and monitor whether it is reassigned again",
                    "score": 8
                },
                {
                    "answerText": "Ask administrators whether temporary access was granted and monitor activity",
                    "score": 5
                },
                {
                    "answerText": "Assume the access is legitimate and continue without further investigation",
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
                    "answerText": "Review scheduled tasks, associated executables, and logs to determine whether persistence mechanisms exist",
                    "score": 17
                },
                {
                    "answerText": "Disable the tasks and monitor whether they reappear during normal operation",
                    "score": 7
                },
                {
                    "answerText": "Restart the system and observe whether scheduled activity continues",
                    "score": 5
                },
                {
                    "answerText": "Assume scheduled tasks are normal and continue monitoring without investigation",
                    "score": 0
                }
            ],
            "feedback": "Reviewing tasks and logs is strongest because it identifies persistence mechanisms. Disabling is reactive. Ignoring is weakest.",
            "shorthand": "Endpoint Issue",
            "longhand": "Unknown scheduled tasks executing",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Review backup configuration, inclusion rules, and recent changes to determine why systems were excluded",
                    "score": 25
                },
                {
                    "answerText": "Run a new backup immediately and monitor whether systems are included",
                    "score": 12
                },
                {
                    "answerText": "Manually back up affected systems and observe whether issues continue",
                    "score": 6
                },
                {
                    "answerText": "Assume occasional backup gaps are normal and continue monitoring without review",
                    "score": 0
                }
            ],
            "feedback": "Reviewing configuration is strongest because it identifies the failure cause. Running backups is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Critical systems missing from backups",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
        },

        {
            "id": "medium_sec_011",
            "question_difficulty": "Medium",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 10},
                "hard": {"allowed": True, "weight": 5}
            },
            "location":  defineCyber,
            "points": 27,
            "question": "Security logs show multiple failed login attempts followed by a successful login for a privileged account. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate failed and successful login events, compare source systems, and determine whether the activity indicates a successful brute force attempt",
                    "score": 27
                },
                {
                    "answerText": "Reset the account password and monitor for additional login attempts during normal usage",
                    "score": 15
                },
                {
                    "answerText": "Lock the account temporarily and observe whether similar login patterns occur again",
                    "score": 8
                },
                {
                    "answerText": "Assume the user entered incorrect credentials multiple times before logging in successfully",
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
                    "answerText": "Trace the external IP activity, examine connection frequency, and determine whether internal systems are consistently communicating with it",
                    "score": 21
                },
                {
                    "answerText": "Block the external address and observe whether internal systems attempt to reconnect",
                    "score": 12
                },
                {
                    "answerText": "Limit outbound traffic temporarily and monitor whether communication patterns change",
                    "score": 6
                },
                {
                    "answerText": "Assume the traffic is routine and continue monitoring without taking action",
                    "score": 0
                }
            ],
            "feedback": "Analyzing traffic is strongest because it identifies potential compromise. Blocking helps but skips investigation. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "Multiple systems contacting unknown external IP",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Map the parent and child processes, check execution context, and determine whether the chain reflects abnormal behavior",
                    "score": 24
                },
                {
                    "answerText": "Terminate the processes and monitor whether similar activity occurs again",
                    "score": 13
                },
                {
                    "answerText": "Restart the endpoint and observe whether the behavior persists during normal operation",
                    "score": 6
                },
                {
                    "answerText": "Assume complex applications are responsible for spawning multiple processes",
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
                    "answerText": "Check file activity timelines, identify the source of changes, and determine whether the behavior matches automated or malicious patterns",
                    "score": 20
                },
                {
                    "answerText": "Restore affected files and monitor whether additional renaming occurs",
                    "score": 11
                },
                {
                    "answerText": "Restrict access to the folder and observe whether file changes stop",
                    "score": 6
                },
                {
                    "answerText": "Assume bulk renaming is part of normal file organization activity",
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
            "location":  defineCyber,
            "points": 23,
            "question": "An account suddenly gains administrative privileges without a recorded request. What should you check first?",
            "choices": [
                {
                    "answerText": "Track privilege assignment history, identify triggering actions, and determine how elevated access was granted",
                    "score": 23
                },
                {
                    "answerText": "Remove elevated privileges and monitor whether access is reassigned",
                    "score": 12
                },
                {
                    "answerText": "Notify administrators and observe whether similar changes occur across accounts",
                    "score": 6
                },
                {
                    "answerText": "Assume the change was part of routine maintenance activity",
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
            "location":  defineCyber,
            "points": 26,
            "question": "An alert indicates potential credential dumping activity on a system. What should you check first?",
            "choices": [
                {
                    "answerText": "Examine memory access behavior, observe related processes, and determine whether credential extraction techniques are present",
                    "score": 26
                },
                {
                    "answerText": "Restart the system and monitor whether similar alerts appear again",
                    "score": 12
                },
                {
                    "answerText": "Isolate the system temporarily and observe whether suspicious behavior continues",
                    "score": 6
                },
                {
                    "answerText": "Assume the alert is related to legitimate administrative tooling activity",
                    "score": 0
                }
            ],
            "feedback": "Analyzing memory and logs is strongest because credential dumping is a critical threat. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Potential credential dumping detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Inspect DNS request patterns, identify domain randomness, and determine whether the behavior aligns with known malware activity",
                    "score": 18
                },
                {
                    "answerText": "Restart the system and observe whether DNS activity returns to expected levels",
                    "score": 8
                },
                {
                    "answerText": "Restrict DNS queries temporarily and monitor whether the volume decreases",
                    "score": 5
                },
                {
                    "answerText": "Assume DNS usage varies based on application behavior and continue monitoring",
                    "score": 0
                }
            ],
            "feedback": "Analyzing DNS patterns is strongest because random queries may indicate malware. Restarting is reactive. Ignoring is weakest.",
            "shorthand": "Network Issue",
            "longhand": "High volume random DNS queries",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Identify which processes are disabling services, check privilege usage, and determine how security controls are being altered",
                    "score": 17
                },
                {
                    "answerText": "Re-enable the services and monitor whether they are disabled again",
                    "score": 8
                },
                {
                    "answerText": "Restart the endpoint and observe whether the services remain active",
                    "score": 5
                },
                {
                    "answerText": "Assume services were temporarily disabled during routine system updates",
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
                    "answerText": "Compare access times with user activity patterns, confirm legitimacy, and determine whether the behavior aligns with expected usage",
                    "score": 19
                },
                {
                    "answerText": "Ask the user about after-hours activity and monitor for additional access attempts",
                    "score": 9
                },
                {
                    "answerText": "Restrict file access temporarily and observe whether access attempts continue",
                    "score": 5
                },
                {
                    "answerText": "Assume users may occasionally work outside normal hours without issue",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because it validates legitimacy. Asking is secondary. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "After-hours sensitive file access",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Validate certificate details, confirm issuer legitimacy, and ensure the domain matches expected values",
                    "score": 16
                },
                {
                    "answerText": "Ask the user to proceed cautiously and report whether the site behaves normally",
                    "score": 6
                },
                {
                    "answerText": "Test access from another system and compare whether the warning appears",
                    "score": 4
                },
                {
                    "answerText": "Assume certificate warnings are normal and continue without verification",
                    "score": 0
                }
            ],
            "feedback": "Validating the certificate is strongest because warnings may indicate interception. Proceeding is risky. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Unexpected certificate warning",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Check system activity, identify what changed the antivirus state, and determine whether unauthorized actions occurred",
                    "score": 14
                },
                {
                    "answerText": "Re-enable antivirus protection and monitor whether it is disabled again",
                    "score": 6
                },
                {
                    "answerText": "Restart the system and observe whether protection remains active",
                    "score": 4
                },
                {
                    "answerText": "Assume antivirus was temporarily disabled during updates",
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
                    "answerText": "Assess DNS server status, confirm resolution paths, and determine whether configuration or service issues are causing failures",
                    "score": 15
                },
                {
                    "answerText": "Restart affected systems and monitor whether name resolution improves",
                    "score": 6
                },
                {
                    "answerText": "Switch DNS servers temporarily and observe whether failures continue",
                    "score": 4
                },
                {
                    "answerText": "Assume occasional DNS issues are normal and continue monitoring",
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
                    "answerText": "Examine execution attempts, identify patterns, and determine whether the successful launch indicates abnormal behavior",
                    "score": 13
                },
                {
                    "answerText": "Restart the endpoint and observe whether application launches stabilize",
                    "score": 6
                },
                {
                    "answerText": "Reinstall the application and monitor whether failures continue",
                    "score": 4
                },
                {
                    "answerText": "Assume application failures are normal under varying system conditions",
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
                    "answerText": "Verify integrity check processes, confirm storage consistency, and determine why discrepancies are appearing",
                    "score": 12
                },
                {
                    "answerText": "Run another backup cycle and monitor whether inconsistencies persist",
                    "score": 5
                },
                {
                    "answerText": "Test recovery of affected files and observe whether issues occur",
                    "score": 3
                },
                {
                    "answerText": "Assume minor inconsistencies do not impact overall data reliability",
                    "score": 0
                }
            ],
            "feedback": "Reviewing logs is strongest because integrity issues may indicate corruption or tampering. Re-running backups is reactive. Ignoring is weakest.",
            "shorthand": "Data Issue",
            "longhand": "Backup integrity inconsistencies detected",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
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
                    "answerText": "Check login attempt details, confirm success status, and determine whether additional suspicious activity is present",
                    "score": 11
                },
                {
                    "answerText": "Have the user change their password and monitor for additional alerts",
                    "score": 5
                },
                {
                    "answerText": "Verify whether the location data is consistent across multiple alerts",
                    "score": 3
                },
                {
                    "answerText": "Assume location data may be inaccurate and continue without action",
                    "score": 0
                }
            ],
            "feedback": "Reviewing login activity is strongest because it confirms compromise status. Resetting is reactive. Ignoring is weakest.",
            "shorthand": "Security Issue",
            "longhand": "Foreign login attempt alert",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": False,
            "repeatable": True
        },

        {
            "id": "hard_sec_001",
            "question_difficulty": "Hard",
            "spawn_rules": {
                "easy": {"allowed": False, "weight": 0},
                "medium": {"allowed": True, "weight": 5},
                "hard": {"allowed": True, "weight": 10}
            },
            "location":  defineCyber,
            "points": 45,
            "question": "Security logs indicate lateral movement activity between multiple internal hosts using valid credentials. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate credential usage across hosts, trace session paths, and determine how access is chaining between systems",
                    "score": 45
                },
                {
                    "answerText": "Force credential resets across affected accounts and observe whether movement between systems continues afterward",
                    "score": 30
                },
                {
                    "answerText": "Isolate one compromised host and watch for new authentication attempts across other systems",
                    "score": 18
                },
                {
                    "answerText": "Assume administrators are performing cross-system tasks and continue monitoring without escalation",
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
                    "answerText": "Map connection timing, originating processes, and callback consistency to determine whether coordinated control traffic is present",
                    "score": 42
                },
                {
                    "answerText": "Block the destination address and observe whether affected systems attempt alternate connections",
                    "score": 28
                },
                {
                    "answerText": "Cycle affected systems and monitor whether periodic connections return during normal operation",
                    "score": 15
                },
                {
                    "answerText": "Assume periodic outbound traffic is related to updates and continue without deeper inspection",
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
            "location":  defineCyber,
            "points": 48,
            "question": "Privileged account activity shows access to multiple high-value systems outside normal patterns. What should you check first?",
            "choices": [
                {
                    "answerText": "Compare access timing, system scope, and privilege usage to determine whether the activity aligns with expected administrative behavior",
                    "score": 48
                },
                {
                    "answerText": "Disable the account and monitor for similar access patterns appearing under different identities",
                    "score": 32
                },
                {
                    "answerText": "Contact the account owner and confirm whether the activity was expected before taking further action",
                    "score": 18
                },
                {
                    "answerText": "Assume broad system access is normal for privileged users and continue without escalation",
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
                    "answerText": "Trace how persistence entries were introduced, including startup paths and execution triggers tied to system changes",
                    "score": 44
                },
                {
                    "answerText": "Remove persistence artifacts and watch for re-creation during subsequent system activity",
                    "score": 30
                },
                {
                    "answerText": "Reimage the system and confirm whether persistence mechanisms reappear after restoration",
                    "score": 18
                },
                {
                    "answerText": "Assume configuration changes are part of normal updates and continue monitoring without action",
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
                    "answerText": "Compare transfer behavior, initiating processes, and destination context to determine whether data movement is unauthorized",
                    "score": 46
                },
                {
                    "answerText": "Block the destination and observe whether alternate transfer attempts occur from the same systems",
                    "score": 30
                },
                {
                    "answerText": "Notify the user tied to the system and confirm whether the transfers were intentional",
                    "score": 18
                },
                {
                    "answerText": "Assume encrypted transfers are expected and continue without further validation",
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
            "location":  defineCyber,
            "points": 41,
            "question": "An alert indicates suspicious PowerShell execution across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Examine execution chains, script origin, and context of use to determine whether commands align with known attack techniques",
                    "score": 41
                },
                {
                    "answerText": "Disable scripting capabilities and observe whether similar behavior appears through alternate methods",
                    "score": 26
                },
                {
                    "answerText": "Restart systems and monitor whether command activity resumes during normal operation",
                    "score": 14
                },
                {
                    "answerText": "Assume scripting usage is administrative in nature and continue without escalation",
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
                    "answerText": "Evaluate query structure, entropy, and frequency patterns to determine whether DNS is being used to encode outbound data",
                    "score": 39
                },
                {
                    "answerText": "Block identified domains and observe whether query patterns shift to new destinations",
                    "score": 25
                },
                {
                    "answerText": "Restart DNS services and monitor whether query behavior stabilizes",
                    "score": 12
                },
                {
                    "answerText": "Assume irregular DNS queries are application-driven and continue monitoring",
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
                    "answerText": "Inspect runtime behavior, memory usage patterns, and process relationships to determine how execution persists without files",
                    "score": 37
                },
                {
                    "answerText": "Reboot the system and observe whether suspicious behavior resumes after startup",
                    "score": 20
                },
                {
                    "answerText": "Run endpoint scans and rely on detection tools to identify any active threats",
                    "score": 10
                },
                {
                    "answerText": "Assume no files indicate no compromise and continue without further action",
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
                    "answerText": "Compare query behavior, modification patterns, and access origin to determine whether changes fall outside application logic",
                    "score": 50
                },
                {
                    "answerText": "Revert recent changes and observe whether unauthorized modifications occur again",
                    "score": 32
                },
                {
                    "answerText": "Restrict database access and monitor whether normal operations are impacted",
                    "score": 18
                },
                {
                    "answerText": "Assume database variability is normal and continue monitoring without action",
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
            "location":  defineCyber,
            "points": 43,
            "question": "An attacker is suspected of using living-off-the-land techniques to evade detection. What should you check first?",
            "choices": [
                {
                    "answerText": "Correlate tool usage patterns, execution context, and system activity to determine whether legitimate utilities are being misused",
                    "score": 43
                },
                {
                    "answerText": "Disable commonly abused tools and observe whether the attacker shifts to alternative techniques",
                    "score": 28
                },
                {
                    "answerText": "Rebuild affected systems and monitor whether similar behavior returns afterward",
                    "score": 16
                },
                {
                    "answerText": "Assume tool usage is expected in normal operations and continue without escalation",
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
            "location":  defineCyber,
            "points": 47,
            "question": "Security logs show suspicious use of built-in administrative tools across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Compare command usage across systems and determine whether legitimate tools are being misapplied",
                    "score": 47
                },
                {
                    "answerText": "Disable administrative utilities across multiple hosts and observe whether activity shifts to alternate execution paths over time",
                    "score": 30
                },
                {
                    "answerText": "Restart affected systems and monitor whether tool usage returns to expected patterns during normal operations",
                    "score": 15
                },
                {
                    "answerText": "Assume tool usage is normal for administrators and continue without escalation",
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
                    "answerText": "Trace outbound connections and identify which services are responsible for initiating them",
                    "score": 40
                },
                {
                    "answerText": "Block outbound traffic from the server and observe whether application functionality is disrupted across dependent services",
                    "score": 28
                },
                {
                    "answerText": "Restart the server and monitor whether outbound communication patterns change during standard operation",
                    "score": 14
                },
                {
                    "answerText": "Assume encrypted traffic is normal and continue without further validation",
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
            "location":  defineCyber,
            "points": 49,
            "question": "An attacker is suspected of harvesting credentials through memory access techniques. What should you check first?",
            "choices": [
                {
                    "answerText": "Examine memory access behavior and determine whether credential extraction patterns are present",
                    "score": 49
                },
                {
                    "answerText": "Reset all credentials across the environment and monitor whether authentication anomalies continue to appear afterward",
                    "score": 32
                },
                {
                    "answerText": "Restart affected systems and observe whether suspicious behavior resumes during operation",
                    "score": 18
                },
                {
                    "answerText": "Assume credential access is part of standard authentication processes",
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
                    "answerText": "Map process relationships and determine how code is being introduced into running processes",
                    "score": 38
                },
                {
                    "answerText": "Terminate affected processes across multiple systems and monitor whether similar behavior returns during continued operation",
                    "score": 24
                },
                {
                    "answerText": "Rebuild the systems entirely and observe whether the issue reappears afterward under normal workloads",
                    "score": 14
                },
                {
                    "answerText": "Assume process interaction is expected in complex applications",
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
                    "answerText": "Compare integrity baselines and determine how unauthorized modifications were introduced",
                    "score": 41
                },
                {
                    "answerText": "Restore files from backup and observe whether unauthorized changes occur again over time during system use",
                    "score": 26
                },
                {
                    "answerText": "Restrict file access broadly and monitor whether system behavior is impacted across users",
                    "score": 15
                },
                {
                    "answerText": "Assume configuration updates caused the changes and continue monitoring",
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
            "location":  defineCyber,
            "points": 44,
            "question": "An attacker is suspected of using token impersonation to access resources. What should you check first?",
            "choices": [
                {
                    "answerText": "Track session behavior and determine whether identity context is being reused improperly",
                    "score": 44
                },
                {
                    "answerText": "Invalidate active sessions across multiple systems and observe whether unauthorized access attempts continue afterward",
                    "score": 28
                },
                {
                    "answerText": "Reset user credentials and monitor whether suspicious access patterns persist across services",
                    "score": 16
                },
                {
                    "answerText": "Assume token usage is routine and continue without investigation",
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
                    "answerText": "Compare traffic paths with segmentation rules and determine how restricted zones are being reached",
                    "score": 36
                },
                {
                    "answerText": "Block communication between affected zones and monitor whether traffic attempts continue between segments",
                    "score": 24
                },
                {
                    "answerText": "Restart network devices and observe whether segmentation behavior returns to expected baselines",
                    "score": 12
                },
                {
                    "answerText": "Assume cross-zone traffic is part of normal operations",
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
                    "answerText": "Examine memory execution patterns and determine how the malware spreads without file artifacts",
                    "score": 37
                },
                {
                    "answerText": "Restart affected systems and monitor whether behavior reappears after reboot across the environment",
                    "score": 22
                },
                {
                    "answerText": "Run endpoint scans across all systems and observe whether detection tools identify the threat",
                    "score": 12
                },
                {
                    "answerText": "Assume lack of files indicates no persistent compromise",
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
                    "answerText": "Compare long-term access patterns and determine whether extraction techniques are present",
                    "score": 39
                },
                {
                    "answerText": "Restrict database access broadly and observe whether extraction activity stops across dependent applications",
                    "score": 25
                },
                {
                    "answerText": "Revert recent changes and monitor whether anomalies continue during future operations",
                    "score": 14
                },
                {
                    "answerText": "Assume database usage varies and continue without escalation",
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
            "location":  defineCyber,
            "points": 43,
            "question": "Security alerts indicate that logging mechanisms are being tampered with across multiple systems. What should you check first?",
            "choices": [
                {
                    "answerText": "Examine logging consistency and determine how visibility is being reduced",
                    "score": 43
                },
                {
                    "answerText": "Restore logging configurations across systems and observe whether tampering continues afterward",
                    "score": 27
                },
                {
                    "answerText": "Restart systems and monitor whether logs begin recording normally during operation",
                    "score": 15
                },
                {
                    "answerText": "Assume logging interruptions are caused by system updates",
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
                    "answerText": "Inspect authentication behavior and determine whether identity tokens are being reused outside expected lifetimes",
                    "score": 50
                },
                {
                    "answerText": "Reset credentials and invalidate sessions across all users to disrupt potential unauthorized access patterns",
                    "score": 32
                },
                {
                    "answerText": "Restart authentication services and observe whether behavior changes across systems",
                    "score": 18
                },
                {
                    "answerText": "Assume ticket-based authentication is functioning normally",
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
                    "answerText": "Compare configurations against baselines and determine how unauthorized routing paths were introduced",
                    "score": 38
                },
                {
                    "answerText": "Restore configuration from backup and monitor whether drift occurs again across the device",
                    "score": 24
                },
                {
                    "answerText": "Restart the device and observe whether routing behavior stabilizes",
                    "score": 12
                },
                {
                    "answerText": "Assume configuration drift is part of maintenance activity",
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
                    "answerText": "Trace application access patterns and determine how sensitive data is being exposed",
                    "score": 37
                },
                {
                    "answerText": "Block the application entirely and observe whether access attempts continue from other sources",
                    "score": 24
                },
                {
                    "answerText": "Restrict user access and monitor whether behavior changes across systems",
                    "score": 12
                },
                {
                    "answerText": "Assume application access differences are configuration-related",
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
            "location":  defineCyber,
            "points": 42,
            "question": "Indicators suggest an attacker is clearing event logs to avoid detection. What should you check first?",
            "choices": [
                {
                    "answerText": "Reconstruct activity timelines and determine how evidence removal is being performed",
                    "score": 42
                },
                {
                    "answerText": "Restore logging systems and observe whether logs are cleared again across multiple systems",
                    "score": 26
                },
                {
                    "answerText": "Restart systems and monitor whether logs begin recording normally during operation",
                    "score": 14
                },
                {
                    "answerText": "Assume logs rotate automatically and continue without action",
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
                    "answerText": "Assess low-level system behavior and determine whether kernel manipulation is present",
                    "score": 36
                },
                {
                    "answerText": "Reimage the system and monitor whether suspicious behavior returns afterward during normal use",
                    "score": 24
                },
                {
                    "answerText": "Run endpoint tools and observe whether threats are detected across scans",
                    "score": 12
                },
                {
                    "answerText": "Assume the alert is a false positive and continue monitoring",
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
            "points": 7,
            "question": "A user reports receiving a suspicious email from a coworker with an unexpected attachment. What steps should you take?",
            "choices": [
                {
                    "answerText": "Verify the message through a separate channel and preserve the email for review",
                    "score": 7
                },
                {
                    "answerText": "Delete the email, warn the user not to open similar attachments, and continue monitoring for related reports",
                    "score": 0
                },
                {
                    "answerText": "Open the attachment in the user session because the sender is internal and the source appears familiar",
                    "score": -6
                }
            ],
            "feedback": "Internal senders can be compromised. Verifying and preserving evidence is strongest. Deleting removes evidence. Opening the attachment risks execution.",
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
                    "answerText": "Isolate the workstation and check endpoint activity for signs of malware execution",
                    "score": 0
                },
                {
                    "answerText": "Restart the workstation, clear temporary files, and ask the user to report if performance problems continue afterward",
                    "score": -3
                },
                {
                    "answerText": "Forward the same attachment to IT staff so they can test whether it behaves the same way elsewhere",
                    "score": -8
                }
            ],
            "feedback": "Containment comes first. Restarting hides symptoms. Forwarding spreads risk.",
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
            "question": "A user says they found a USB drive in the office and wants to know if they can check what is on it. What steps should you take?",
            "choices": [
                {
                    "answerText": "Do not connect it and route the device through approved security handling procedures",
                    "score": 6
                },
                {
                    "answerText": "Label the device, place it aside, and wait until someone can inspect it later",
                    "score": 0
                },
                {
                    "answerText": "Plug it into the workstation briefly to identify the owner while avoiding suspicious files or unknown folders",
                    "score": -5
                }
            ],
            "feedback": "Unknown media is unsafe. Prevent connection. Delaying helps slightly. Plugging in can trigger attacks.",
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
                    "answerText": "Disconnect the system and check recent device activity tied to the unknown process",
                    "score": 0
                },
                {
                    "answerText": "End the unfamiliar process, remove the USB device, and allow the user to keep working while monitoring",
                    "score": -3
                },
                {
                    "answerText": "Copy the USB contents to a shared folder so security staff can inspect the files remotely",
                    "score": -8
                }
            ],
            "feedback": "Containment is required. Ending a process is incomplete. Copying spreads risk.",
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
            "question": "A user reports repeated MFA prompts they did not request. What steps should you take?",
            "choices": [
                {
                    "answerText": "Deny active prompts and secure the account before any prompt is approved",
                    "score": 8
                },
                {
                    "answerText": "Tell the user to ignore the prompts for now and report back if they continue for several hours",
                    "score": 0
                },
                {
                    "answerText": "Approve one prompt to determine whether the notifications stop and confirm whether the request is legitimate",
                    "score": -7
                }
            ],
            "feedback": "Unexpected MFA prompts indicate attack attempts. Secure immediately. Ignoring delays. Approving grants access.",
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
                    "answerText": "Revoke active sessions, reset credentials, and check recent account activity",
                    "score": 0
                },
                {
                    "answerText": "Ask the user to watch for more alerts and report if another unfamiliar login appears later",
                    "score": -3
                },
                {
                    "answerText": "Disable MFA temporarily so the user no longer receives confusing prompts during future sign-ins",
                    "score": -8
                }
            ],
            "feedback": "Account is compromised. Revoke and reset. Waiting allows access. Disabling MFA weakens security.",
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
            "question": "Sensitive documents are found unattended on a shared printer. What steps should you take?",
            "choices": [
                {
                    "answerText": "Secure the documents and identify the owner before determining possible exposure",
                    "score": 5
                },
                {
                    "answerText": "Place the documents beside the printer so the owner can find them when they return",
                    "score": 0
                },
                {
                    "answerText": "Throw the documents away immediately so nobody else can read the sensitive information later",
                    "score": -4
                }
            ],
            "feedback": "Secure and track exposure. Leaving documents risks access. Destroying them removes accountability.",
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
                    "answerText": "Document known details, check print logs, and identify the likely owner",
                    "score": 0
                },
                {
                    "answerText": "Ask nearby employees whether they remember seeing the documents before they were discarded",
                    "score": -2
                },
                {
                    "answerText": "Report that there is no issue because the documents are no longer visible or available",
                    "score": -6
                }
            ],
            "feedback": "Reconstruct exposure using logs. Asking others is unreliable. Ignoring impact is incorrect.",
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
            "question": "A user reports that their browser redirects searches to unfamiliar websites. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check extensions, DNS behavior, and recent changes that could explain the redirects",
                    "score": 9
                },
                {
                    "answerText": "Reset the homepage and default search engine, then monitor whether the redirects continue afterward",
                    "score": 0
                },
                {
                    "answerText": "Allow normal browsing because redirects are often caused by advertising networks, regional pages, or website settings",
                    "score": -6
                }
            ],
            "feedback": "Redirects may indicate compromise. Investigate cause. Resetting hides symptoms. Continuing increases risk.",
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
                    "answerText": "Reset the credentials and check the system for browser or DNS compromise",
                    "score": 0
                },
                {
                    "answerText": "Clear browsing data and ask the user to avoid unfamiliar websites going forward",
                    "score": -3
                },
                {
                    "answerText": "Retry logging into the same site to confirm whether the credentials were accepted successfully",
                    "score": -8
                }
            ],
            "feedback": "Treat credentials as exposed. Clearing data does not secure the account. Retrying login risks further compromise.",
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
            "location":  defineCyber,
            "points": 22,
            "question": "Multiple users report receiving similar phishing emails that appear to come from an internal department account. What steps should you take?",
            "choices": [
                {
                    "answerText": "Preserve samples, check sender status, and determine whether the internal account is compromised",
                    "score": 22
                },
                {
                    "answerText": "Tell users to delete the emails, avoid clicking links, and wait to see if more reports arrive",
                    "score": 0
                },
                {
                    "answerText": "Trust the messages because they came from an internal department account and ask users to follow the instructions carefully",
                    "score": -14
                }
            ],
            "feedback": "Internal sources can be compromised. Preserving samples and validating the account is strongest. Deleting removes evidence. Trusting the email enables the attack.",
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
            "location":  defineCyber,
            "points": 0,
            "question": "The internal sender account was trusted, and several users entered credentials through the linked page. How do you recover?",
            "choices": [
                {
                    "answerText": "Reset exposed credentials, revoke sessions, and contain the compromised sender account",
                    "score": 0
                },
                {
                    "answerText": "Send a reminder telling users not to click future links while waiting for more suspicious activity",
                    "score": -8
                },
                {
                    "answerText": "Delete the reported emails from mailboxes without checking which users submitted credentials through the linked page",
                    "score": -18
                }
            ],
            "feedback": "Treat both credentials and the sender account as compromised. Resetting and revoking limits access. Waiting delays response. Deleting emails removes evidence and leaves compromised users active.",
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
            "question": "Network monitoring shows high outbound traffic from a single workstation to an unfamiliar external address. What steps should you take?",
            "choices": [
                {
                    "answerText": "Identify the process, check the destination, and determine whether the traffic suggests data exfiltration",
                    "score": 20
                },
                {
                    "answerText": "Restart the workstation and monitor whether outbound traffic returns to normal after the reboot",
                    "score": 0
                },
                {
                    "answerText": "Ignore the traffic spike because workstations may upload large files during normal business activity or cloud synchronization",
                    "score": -12
                }
            ],
            "feedback": "High outbound traffic can indicate exfiltration. Identifying the source is strongest. Restarting hides evidence. Ignoring allows potential data loss.",
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
                    "answerText": "Isolate the workstation and capture current traffic and process activity before remediation",
                    "score": 0
                },
                {
                    "answerText": "Restart the workstation again and wait longer before allowing the user to sign back in",
                    "score": -7
                },
                {
                    "answerText": "Allow the user to continue working because the reboot did not permanently damage the system or block access",
                    "score": -16
                }
            ],
            "feedback": "Containment and observation are required. Repeating restarts loses evidence. Allowing use risks continued exfiltration.",
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
            "question": "Audit logs show a user downloading many sensitive files shortly before leaving the company. What steps should you take?",
            "choices": [
                {
                    "answerText": "Preserve logs, compare access patterns, and assess whether the downloads indicate data theft",
                    "score": 24
                },
                {
                    "answerText": "Ask the user directly whether they needed the files and continue monitoring if they say it was legitimate",
                    "score": 0
                },
                {
                    "answerText": "Delete the user's downloaded copies remotely without preserving logs or checking the full scope of accessed data",
                    "score": -15
                }
            ],
            "feedback": "Preserve evidence first. Insider risk requires validation. Asking the user may alert them. Deleting data removes evidence.",
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
                    "answerText": "Preserve remaining evidence and coordinate with management to assess exposure",
                    "score": 0
                },
                {
                    "answerText": "Wait to see if the user downloads more files before escalating the situation further",
                    "score": -8
                },
                {
                    "answerText": "Delete the user's account immediately without checking what data may already have been copied or accessed",
                    "score": -18
                }
            ],
            "feedback": "Preserve what remains and assess impact. Waiting risks further loss. Deleting the account removes visibility.",
            "shorthand": "Data Issue",
            "longhand": "Insider activity disrupted before preservation",
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
            "question": "An endpoint alert shows an unknown scheduled task running under a normal user account. What steps should you take?",
            "choices": [
                {
                    "answerText": "Check the task details, linked executable, and recent activity for signs of persistence",
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
            "feedback": "Scheduled tasks are common persistence methods. Investigating is strongest. Disabling hides symptoms. Whitelisting enables compromise.",
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
                    "answerText": "Isolate the endpoint and check task creation events, executables, and parent processes",
                    "score": 0
                },
                {
                    "answerText": "Disable the new task and continue repeating that process if it appears again",
                    "score": -7
                },
                {
                    "answerText": "Whitelist the new task name so repeated alerts stop interrupting the user during normal work",
                    "score": -16
                }
            ],
            "feedback": "Recurring tasks indicate persistence. Investigate root cause. Repeating fixes fails. Whitelisting hides the threat.",
            "shorthand": "Endpoint Issue",
            "longhand": "Scheduled task persistence returns",
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
            "location":  defineCyber,
            "points": 26,
            "question": "A privileged account shows a successful login shortly after many failed attempts from the same source. What steps should you take?",
            "choices": [
                {
                    "answerText": "Correlate failed and successful logins and determine whether the access was unauthorized",
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
            "feedback": "This pattern suggests compromise. Correlation reveals scope. Resetting helps but misses activity. Ignoring is dangerous.",
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
            "location":  defineCyber,
            "points": 0,
            "question": "The password was reset, but the account had already accessed several sensitive systems. How do you recover?",
            "choices": [
                {
                    "answerText": "Revoke active tokens and determine what actions occurred after the login",
                    "score": 0
                },
                {
                    "answerText": "Assume the password reset resolved the issue and continue monitoring for future login failures",
                    "score": -8
                },
                {
                    "answerText": "Delete authentication logs to reduce confusion and avoid duplicate investigation of the same account activity",
                    "score": -20
                }
            ],
            "feedback": "Assess impact after compromise. Reset alone is insufficient. Ignoring misses damage. Deleting logs destroys evidence.",
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
            "location":  defineCyber,
            "points": 46,
            "question": "Logs indicate possible lateral movement using valid admin credentials across multiple servers. What steps should you take?",
            "choices": [
                {
                    "answerText": "Correlate authentication paths and determine how access is moving between systems",
                    "score": 46
                },
                {
                    "answerText": "Reset administrator credentials across all systems and monitor logs for additional lateral movement attempts afterward",
                    "score": 0
                },
                {
                    "answerText": "Assume the activity is legitimate because administrators often access multiple systems during normal operations",
                    "score": -20
                }
            ],
            "feedback": "Valid credentials do not imply legitimate behavior. Mapping movement reveals scope. Resetting limits access but reduces visibility. Ignoring allows compromise to continue.",
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
            "location":  defineCyber,
            "points": 0,
            "question": "The password was reset, but logs show continued movement using existing sessions. How do you recover?",
            "choices": [
                {
                    "answerText": "Revoke active sessions and trace system access to identify persistence mechanisms",
                    "score": 0
                },
                {
                    "answerText": "Reset credentials again across all systems and monitor whether the activity eventually stops",
                    "score": -8
                },
                {
                    "answerText": "Ignore session activity since password resets should prevent unauthorized access from continuing",
                    "score": -22
                }
            ],
            "feedback": "Active sessions remain valid after resets. Revoking sessions removes access. Repeating resets fails. Ignoring allows persistence.",
            "shorthand": "Access Issue",
            "longhand": "Active sessions persist after credential reset",
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
            "question": "A critical server shows sustained encrypted outbound traffic to unknown destinations. What steps should you take?",
            "choices": [
                {
                    "answerText": "Examine traffic patterns and determine whether the activity represents data exfiltration",
                    "score": 44
                },
                {
                    "answerText": "Block all outbound traffic from the server and observe how system functionality is impacted across services and users",
                    "score": 0
                },
                {
                    "answerText": "Ignore the traffic because encryption is commonly used and does not indicate malicious activity by itself",
                    "score": -18
                }
            ],
            "feedback": "Encryption does not equal safety. Analysis reveals intent. Blocking reduces visibility. Ignoring risks data loss.",
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
                    "answerText": "Determine what data was transferred and identify affected systems and destinations",
                    "score": 0
                },
                {
                    "answerText": "Keep traffic blocked and assume the issue is resolved without further investigation into prior activity",
                    "score": -10
                },
                {
                    "answerText": "Restore connectivity and test whether the same transfer behavior appears again under normal operating conditions",
                    "score": -20
                }
            ],
            "feedback": "Containment does not undo exposure. Assess damage. Assuming resolution ignores impact. Restoring connectivity risks recurrence.",
            "shorthand": "Data Issue",
            "longhand": "Exfiltration occurred before containment",
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
            "question": "Endpoint telemetry shows fileless malware activity with no disk artifacts present. What steps should you take?",
            "choices": [
                {
                    "answerText": "Examine memory behavior and determine how execution is occurring without files",
                    "score": 48
                },
                {
                    "answerText": "Restart the system and monitor whether the behavior returns after reboot during normal operation",
                    "score": 0
                },
                {
                    "answerText": "Ignore the alert because no files exist on disk and no persistent malware appears to be installed",
                    "score": -22
                }
            ],
            "feedback": "Fileless threats exist in memory. Analysis is required. Restarting removes evidence. Ignoring allows persistence.",
            "shorthand": "Endpoint Issue",
            "longhand": "Fileless malware activity detected",
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
                    "answerText": "Analyze the system while active to identify persistence and execution mechanisms",
                    "score": 0
                },
                {
                    "answerText": "Restart the system again and wait longer before allowing normal usage",
                    "score": -9
                },
                {
                    "answerText": "Assume the issue resolved temporarily and continue operations without further investigation",
                    "score": -20
                }
            ],
            "feedback": "Active analysis is required. Reboots remove evidence. Ignoring allows persistent threats.",
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
            "question": "Database logs show subtle, continuous extraction of small amounts of sensitive data over time. What steps should you take?",
            "choices": [
                {
                    "answerText": "Compare query patterns and determine whether the behavior indicates stealthy data exfiltration",
                    "score": 43
                },
                {
                    "answerText": "Restrict database access temporarily and observe whether the extraction behavior stops over time",
                    "score": 0
                },
                {
                    "answerText": "Ignore the activity because small transfers are typical for database queries and application usage",
                    "score": -17
                }
            ],
            "feedback": "Small transfers can indicate stealth exfiltration. Pattern analysis reveals intent. Restricting hides behavior. Ignoring allows loss.",
            "shorthand": "Data Issue",
            "longhand": "Gradual data extraction detected",
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
                    "answerText": "Determine the scope of exposed data and initiate breach response procedures",
                    "score": 0
                },
                {
                    "answerText": "Restore database permissions and assume the restriction resolved the issue going forward",
                    "score": -10
                },
                {
                    "answerText": "Delete database logs to simplify the environment and prevent confusion during investigation",
                    "score": -25
                }
            ],
            "feedback": "Assess exposure and respond. Assuming resolution ignores damage. Deleting logs destroys evidence.",
            "shorthand": "Data Issue",
            "longhand": "Confirmed exfiltration before restriction",
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
            "location":  defineCyber,
            "points": 50,
            "question": "Logs indicate that security logging services are being disabled across multiple systems. What steps should you take?",
            "choices": [
                {
                    "answerText": "Determine how logging is being disabled and identify whether activity is attempting to evade detection",
                    "score": 50
                },
                {
                    "answerText": "Re-enable logging across systems and monitor whether it is disabled again during normal operation",
                    "score": 0
                },
                {
                    "answerText": "Ignore the issue because logging services may stop and restart during updates or maintenance cycles",
                    "score": -20
                }
            ],
            "feedback": "Loss of visibility is critical. Determine cause. Re-enabling is temporary. Ignoring removes detection.",
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
            "location":  defineCyber,
            "points": 0,
            "question": "Logging was restored, but gaps exist during the period it was disabled. How do you recover?",
            "choices": [
                {
                    "answerText": "Reconstruct activity using available data and determine what occurred during the gap",
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
            "feedback": "Reconstruct events to understand impact. Assuming safety is risky. Clearing logs destroys evidence.",
            "shorthand": "Security Issue",
            "longhand": "Log gap after disruption",
            "followup_event": {"allowed": False, "event_id": "", "score_cutoff": 0},
            "is_followup": True,
            "repeatable": False
        }
    ]
    return
