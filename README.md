# Osu Daily Challenge Scraper

A web scraper script made in Python using Selenium WebDrivers. The script scrapes all of the osu! [daily challenge](https://osu.ppy.sh/rankings/daily-challenge/) beatmap links to date and formats the URLs into a text file.

There is really no real use or need for this, just a fun project for myself 🤓

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Firefox browser installed.
- Geckodriver installed and added to your system PATH.
- Selenium package installed. You can install it using pip:

```bash
pip install selenium
```
## Usage

Run the script, the input and output files will be created automatically

You can change the sleep timer for a faster output, but you may face the CAPTCHA boss 😧

you can comment out this line if you would like to see the window as it scrapes the links

```java
options.add_argument("--headless")
```

## TODO

 - Fix timer (or remove it)
 - Create a chrome-compatible script
 - Adjust for a specified date range
 - Provide links for the specific difficulty used in the challenge
 - Output the files to SQL or CSV for database purposes
 - Bypass CAPTCHA for insane speeds

## License

This project is open-source and available under the MIT License.

Feel free to modify any sections as needed, especially the script execution details or any specific instructions related to your development environment!
