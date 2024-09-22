# Text to Event Tool

<p align="center">
  <img src="media/banner.png" alt="2" width="400">
</p>

<p align="center">
<b>Text to Event! Convert natural language descriptions of events into Google Calendar events. </b>
</p>

<p align="center">
<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#configuration-options">Configuration</a> •
  <a href="#credits">Credits</a>
  <a href="#related">Related</a>
  <a href="#about-the-core-contributors">About the Core Contributors</a>
</p>

</p>

<p align="center">
  <img src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FPython-Template%2Fmain%2Fpyproject.toml&query=%24.project.name&label=Project Name&color=purple" alt="Dynamic TOML Badge">
  <img alt="Project Version" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FPython-Template%2Fmain%2Fpyproject.toml&query=%24.project.version&label=version&color=blue">
  <img alt="Python Version" src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FPython-Template%2Fmain%2Fpyproject.toml&query=%24.project['requires-python']&label=python&logo=python&color=blue">
  <img src="https://img.shields.io/badge/License-MIT-blue" alt="License">
  <img alt="Dynamic YAML Badge" src="https://img.shields.io/badge/dynamic/yaml?url=https%3A%2F%2Fraw.githubusercontent.com%2FMiyamura80%2FPython-Template%2Fmain%2Fglobal_config%2Fglobal_config.yaml&query=%24%5B%27model_name%27%5D&label=Model in Use&color=yellow">
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Miyamura80/Python-Template">
  <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/Miyamura80/Python-Template/test_target_tests.yaml?branch=main">

</p>

--- 

<p align="center">
  <img src="media/demo.gif" alt="2" width="800">
</p>


## Key features

- Convert natural language descriptions of events into Google Calendar events. Chat descriptions, etc.


## Quick Start

- Install dependencies:
  ```
  rye sync
  ```

- Run the script:
  ```
  rye run python main.py
  ```
  - Optional: If you want to use a more convenient shorthand, via the CLI, follow the instructions below:
    - Get the current `pwd`:  
      ```
      pwd
      ```
    - Open `.zshrc` or `.bashrc`:
      ```
      nano ~/.zshrc
      ```
    - Add the following to your `.zshrc` or `.bashrc`:
      ```
      alias schedule='cd /path/to/pwd && rye run python main.py'
      ```
    - Reload the shell:
      ```
      source ~/.zshrc
      ```
    - Now, you can use `schedule` to run the script from anywhere in the terminal.
      ```
      schedule
      ```


## Configuration Options

1. Global config: [`global_config/global_config.yaml`](global_config/global_config.yaml)
2. Test config: [`tests/config.yaml`](tests/config.yaml) - these are configurations specific to the tests.
3. Environment Variables: Store environmnent variables in `.env` (Create this if not exists) and `global_config/global_config.py`  will read those out automatically. Then, you can import them as follows:

    `.env` file:
    ```env
    OPENAI_API_KEY=sk-...
    ```
    python file:
    ```python
    from global_config import global_config

    print(global_config.OPENAI_API_KEY)
    ```

## Credits

This software uses the following open source packages:
- [Cursor: The AI Code Editor](cursor.com)
- [Rye: a Hassle-Free Python Experience](https://rye.astral.sh/)


## Related

Coming soon...

## You may also like...

Coming soon...


## About the core contributors

- Eito Miyamura is a Co-Founder & CEO of [GatlingX](x.com/gatling_x), formerly CS, AI, RL MSc at University of Oxford. Interested in ML/RL/Robotics/Zero Knowledge, Blockchain networks. [![Follow me on twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Eito_Miyamura)
