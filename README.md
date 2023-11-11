# Bulk Downloader

This is a bulk downloader system. To use it, follow the steps below:

1. Put all the files you want to download in the `./files` directory.
2. Start the server using Flask or Gunicorn.
3. Navigate to the index route in your web browser.

The system will automatically download all the files in the `./files` directory.

## Configuration

Flask configuration is stored in './conf.py' as a kwargs dictionary. Gunicorn configuration is not included in this repository but can be found in the Gunicorn documentation.

## Requirements

- Python 3.6+
- Flask
- Gunicorn (optional)
- A web browser