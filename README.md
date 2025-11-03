# DeepSeek Android Chat App

This project is a simple Android chat application built with **Python** and **Kivy**. It demonstrates how to create a mobile user interface and interact with the [DeepSeek API](https://api.deepseek.com) to have conversations with a large language model.

## Features

- Simple chat interface with message history
- Calls the DeepSeek `/chat/completions` endpoint via HTTP
- Uses the `requests` library instead of the official OpenAI SDK
- Written entirely in Python using Kivy for cross-platform UI
- Can be packaged into an APK using Buildozer

## Prerequisites

- Python 3.9+ installed on your development machine
- [Kivy](https://kivy.org/) and [requests](https://requests.readthedocs.io/) Python packages (see `requirements.txt`)
- A DeepSeek API key – you can apply for one on the [DeepSeek platform](https://platform.deepseek.com).  
  *Do not commit your API key into version control!* The code reads the key from the `DEEPSEEK_API_KEY` environment variable. You can also replace the `'YOUR_DEEPSEEK_API_KEY'` placeholder in `main.py`.

## Running on Desktop

Clone this repository and install dependencies:

```bash
git clone https://github.com/Ptttt1t/deepseek-android-chat.git
cd deepseek-android-chat
pip install -r requirements.txt
```

Set your API key and launch the app:

```bash
export DEEPSEEK_API_KEY=sk-your-api-key
python main.py
```

You will see a window with a text input and a send button. Type messages and the app will display responses from the DeepSeek model.

## Building an Android APK

This repository includes a basic `buildozer.spec` file that describes how to package the app for Android. To build an APK:

1. Install [Buildozer](https://github.com/kivy/buildozer):

   ```bash
   pip install buildozer
   ```

2. Ensure you have the Android SDK/NDK and other requirements installed (Buildozer will prompt you on first run).

3. From the project directory, initialize buildozer (if you haven't already):

   ```bash
   buildozer init
   ```

   A `buildozer.spec` file will be generated. The provided spec in this repository contains default settings and declares the `INTERNET` permission for API access.

4. Build the APK:

   ```bash
   buildozer android debug
   ```

   The first build may take some time as it downloads the Android toolchain. Once finished, the APK will be located in the `bin` directory.

5. Transfer the APK to your Android device and install it. On first launch, the app will attempt to call the DeepSeek API using the environment variable or placeholder key.

## Customization

- To maintain conversation history across multiple turns, modify the `ChatLayout` class to keep a list of previous messages and include them in the `messages` array sent to the API.
- For streaming responses, set the `stream` parameter to `True` and process the streaming chunks accordingly.
- To change the UI appearance or layout, edit the Kivy string defined in `main.py`.

## License

This project is provided for educational purposes without a specific license. You are free to modify and use it as a starting point for your own projects.
