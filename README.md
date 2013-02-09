Sublime-Hhhhold 1.0
=============================

Hhhhold.com placeholder plugin for Sublime Text 2

A plugin using the features of [hhhhold!](http://hhhhold.com)
* Can insert an image tag with dummy image
* Can store images locally to improve development speed and limit requests
* Can insert any sized image tag with dummy image
* Can browse and insert locally stored hhhhold.com images
* Sizes, Formats,  can all be configured in the settings

### Version 1.0
* Initial release

## Installation
### Package Control
If you have [Package Control](http://wbond.net/sublime_packages/package_control) installed

* search for "Hhhhold.com Placeholder Image Tag Generator" to install it

### Using Git
Go to your Sublime Text 2 Packages directory and clone the repository using the command below:

    git clone https://github.com/ThisIsJohnBrown/Sublime-hhhhold

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Hhhhold.com Placeholder Image Tag Generator`
* Copy the folder to your Sublime Text 2 `Packages` directory

## How to use
* Launch the Command Palette using the menu (Tools->Command Palette...) or short key-command Shift+Cmd+P
* Be sure to look through the settings before use
* h, h, tab (to insert image)
* Find "Hhhhold insert default size" (for default sized image)
* Find "Hhhhold insert size range" (to see the hhhhold.com ranges)
* Find "Hhhhold insert cached images" (to browse and insert cached images)

## Settings
Find the settings file in the menu: Sublime Text2 ~> Preferences ~> Package Settings ~> Hhhhold ~> Settings
* `hh_size` The default size of the image, for quick insert
* `hh_default_sizes` List of image sizes to insert
* `hh_format` File format. You can use png, gif or jpg
* `hh_localimages` true/false if you want to save the dummy images locally
* `hh_imagepath` The path for your image folder in your web project. This is where the dummy images is stored

### Using key-commands
* h, h, tab (to insert image)
