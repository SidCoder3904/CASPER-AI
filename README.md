# C.A.S.P.E.R - Cognitive Adaptive Speech-enabled Personal Evolving Robot

CASPER is an offline Personal AI Assistant designed to help with daily tasks without relying on an internet connection. It features voice-to-voice communication using NLP techniques, an interactive GUI, and background processing, making it a versatile tool for task automation and personalized support.

## Features

- **Open/Close Apps:** Quickly open or close applications using voice commands.
- **Send Emails:** Send emails effortlessly with simple voice instructions.
- **Date/Time/Calendar:** Get the current date, time, and calendar details.
- **Jokes:** Enjoy a bit of humor with random jokes.
- **Enable/Disable/Change Wakeword:** Customize the assistant's wakeword to your preference.
- **Website Opening:** Open websites directly through voice commands.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CASPER-AI.git
    cd CASPER-AI
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the project environment:
    - Ensure you have the necessary dependencies like `pyttsx3`, `SpeechRecognition`, `CustomTkinter`, `AppOpener`, and others listed in `requirements.txt`.

4. Run the assistant:
    ```bash
    python casper.py
    ```

## Usage

Upon launching CASPER, you can interact with it using voice commands. CASPER supports a variety of tasks, including opening apps, sending emails, and more. The GUI allows for easy interaction, and the background processing ensures a smooth user experience.

## Customization

- **Wakeword:** You can enable, disable, or change CASPER's wakeword to fit your needs.
- **Email Setup:** Customize the email functionality by setting up the sender's credentials in the code.
- **Application Directory:** Update the `app_dir` and `website_dir` dictionaries in `keyword.py` with your preferred apps and websites for seamless operation.

