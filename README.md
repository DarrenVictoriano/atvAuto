# Android TV Automation Tool with GUI

### Overview

This is an automation tool based on `DAAF` framework, `atvAuto` added a Graphical User Interface to be able to see clearly the current test case running

### How to use:

*Requirements:*
* Python3 and Android Platform tools (ADB) are installed and in PATH.
* Clone or Download this Repo

*Running Script:*
* All the Python file in root folder are pre-made script, simply run it via Python terminal

        c:\atvAuto> python demo.py


* You should see the screen below; Enter how many loops you want the script to repeat then click "Start" button
![demo.py](https://raw.githubusercontent.com/DarrenVictoriano/atvAuto/master/img/demo_screenshot.PNG)


### How to make your own:
1. Create a new python file inside the root folder /atvAuto.
2. Copy the code from the file template.py to your new script file.
3. Update the boilerplate like below:

   * First the `__init__` function, change the "Template" text, this will be the Title Header of the script. And set the `self.playback_time` based on long you want the script to playback the content. (this takes a number equivalent to minutes of playback)

            def __init__(self, tkRoot):
                """ Initialize the UI and then Set Title Header"""
                # Update the string "Template" to your desired Title
                super().__init__(tkRoot, "Template")

                # this is in minutes
                self.playback_time = 1

   * Second, the `testCaseInfo` function, this contains the instruction shown on the left side of the script, Each call of the 'makeInstructionLabel' function is one new line.

                def testCaseInfo(self):
                        """ 
                        Set the test case info
                        This is the one that shows on the left side of the screen
                        Each call of the 'makeInstructionLabel' is one line
                        """
                        self.makeInstructionLabel("Press Power Key")
                        self.makeInstructionLabel("Wait 5 seconds")

   * Lastly, the `runThis` function, is where the test cases will be assembled: For more info about the test cases see the documentation below.

                def runThis(self):
                        """
                        Below is where you assemble test cases
                        """

                        # Press RC POWER Key
                        self.press_rc_key("POWER")
                        self.wait_second(3)


<br>

___
## Documentation:

Below is a list of pre-defined test cases that you can use for creating an automation script inside the function `runThis`

* Pause and Input
   * **self.wait_second(time)** - Pause for a specified `time` as seconds.
   * **self.wait_minute(time)** - Pause for a specified `time` as minutes.
   * **self.launch_tv_input()** - Press TV RC key.
   * **self.launch_hdmi_input("INPUT KEYCODES")** - Launch the specified HDMI keycode. Must be a string. (Check the Special keycodes for input in the List of RC Keycodes)

* Press RC Keys
   * **self.channel_down()** - Press Channel Down RC key.
   * **self.channel_up()** - Press Channel Up RC key.
   * **self.volume_down()** - Press Volume Down RC key.
   * **self.volume_up()** - Press Volume Up RC key.
   * **self.press_home()** - Press Home RC key.
   * **self.press_ff()** - Press Fast Forward RC Key.
   * **self.press_rw()** - Press Rewind RC Key.
   * **self.press_play()** - Press Play RC Key.
   * **self.press_rc_key("RC KEYCODE")** - Press the specified RC keycode, must be a string. Check RC Keycodes below (SonyRCKey)

* Launch and Playback Apps
  * **self.launch_netflix()** - Launch Netflix using ADB `am start` command, this will clear the app from memory before launching it.
  * **self.select_netflix_content()** - Select a content for netflix then start playback.
  * **self.playback_netflix(time)** - Pause the script to let the content plaback for the specified `time` as minutes.

  * **self.launch_amazon()** - Launch Netflix using ADB `am start` command, this will clear the app from memory before launching it.
  * **self.select_amazon_content()** - Select a content for amazon then start playback.
  * **self.playback_amazon(time)** - Pause the script to let the content plaback for the specified `time` as minutes.

  * **self.launch_hulu()** - Launch Netflix using ADB `am start` command, this will clear the app from memory before launching it.
  * **self.select_hulu_content()** - Select a content for hulu then start playback.
  * **self.playback_hulu(time)** - Pause the script to let the content plaback for the specified `time` as minutes.

  * **self.launch_vudu()** - Launch Netflix using ADB `am start` command, this will clear the app from memory before launching it.
  * **self.select_vudu_content()** - Select a content for vudu then start playback.
  * **self.playback_vudu(time)** - Pause the script to let the content plaback for the specified `time` as minutes.

  * **self.launch_youtube()** - Launch Netflix using ADB `am start` command, this will clear the app from memory before launching it.
  * **self.select_youtube_content()** - Select a content for youtube then start playback.
  * **self.playback_youtube(time)** - Pause the script to let the content plaback for the specified `time` as minutes.


<br>

___
### List of RC Keycodes

        # How to read
        KEYCODE - Description

        POWER - Press Power key
        INPUT - Press Inpout  key
        BRAIVA_SYNC_MENU - Press Sync Menu key
        STB_MENU - Press STB Menu key

        NUMBER_0 - Press 0
        NUMBER_1 - Press 1
        NUMBER_2 - Press 2
        NUMBER_3 - Press 3
        NUMBER_4 - Press 4
        NUMBER_5 - Press 5
        NUMBER_6 - Press 6
        NUMBER_7 - Press 7
        NUMBER_8 - Press 8
        NUMBER_9 - Press 9
        DOT - Press (.)

        GOOGLE_PLAY - Press Google Play key
        NETFLIX - Press Netflix key
        YOUTUBE - Press YouTube key
        YELLOW - Press Yellow key
        BLUE - Press Blue key
        RED - Press Red key
        GREEN - Press Green key

        ACTION_MENU - Press Action Menu key
        GUIDE - Press Guide key
        APPS - Press Apps key
        BACK - Press Back key
        HOME - Press Home key
        TV - Press TV key

        UP - Press Up key
        DOWN - Press Down key
        LEFT - Press Left key
        RIGHT - Press Right key
        ENTER - Press Enter key

        VOLUME_UP - Press Volume Up key
        VOLUME_DOWN - Press Volume Down key
        JUMP - Press Jump key
        MUTE - Press Mute key
        CHANNEL_UP - Press Channel Up key
        CHANNEL_DOWN - Press Channel Down key

        AUDIO - Press Audio key
        FF - Press Fast Forward key
        PLAY - Press Play key
        RW - Press Rewind key
        SUBTITLE - Press CC/Close caption key
        PREV - Press Previous key
        PAUSE - Press Pause key
        NEXT - Press Next key
        HELP - Press Help key
        WIDE - Press Wide Mode key
        STOP - Press Stop key

        # Special Keycodes to launch Inputs, used by `self.launch_hdmi_input()`
        HDMI1 - Tune to HDMI1
        HDMI2 - Tune to HDMI2
        HDMI3 - Tune to HDMI3
        HDMI4 - Tune to HDMI4
        VIDEO - Tune to Video