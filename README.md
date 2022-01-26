# ToProfile

Finished rendering the frames of that animation, and now the colors look washed out and ugly? This terminal program will solve exactly that.

## Details
* Uses Python's `PIL` library to transform the effects of a color profile to another
* Has capability of processing entire folders of images automatically

![nice image](https://i.ibb.co/7KP1VKZ/Image-1-26-22-at-4-29-PM.jpg)

## How to Install
1. Download the code and unzip it
2. Edit your terminal configuration file to contain the path to `toprofile.sh` in this repository:

        source ~/path/to/shell/file/toprofile/toprofile.sh

## Usage
**If this is your first time using the tool, scroll down to the Configuration section**

To use the command, simply type it's name, followed by a path, if needed.

    > toprofile                      # Tranform all images in current working directory
    > toprofile path/to/dir          # Transform all images in the referenced directory
    > toprofile path/to/image.png    # Transform only the referenced image
        
## Configuration
Before using the program, you must first specify what color profiles to use by giving the program the paths of the color profile files. They will be saved.
<pre>
> toprofile -config
> Configure color profile paths? (y/n) <b>y</b>
> Abs. path of viewing profile? <b>/Library/ColorSync/Profiles/Displays/LG HDR 4K-1E6E6CBA-3BC9-4271-993A-8C19340DBF79.icc</b>
> Abs. path of display profile? <b>/System/Library/Colorsync/Profiles/sRGB Profile.icc</b>
> Configuration successfully saved
</pre>
In this example, I've provided my monitor's color profile and the standard sRGB color profile. When I run the command, images will be **saved using the `display profile`**. However, they will **appear as if they use the `viewing profile`.** In this case, I am saving the images as sRGB, while retaining the effect of my monitor's color profile.

      
