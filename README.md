# MIDI2Tuneshare
This Program helps people to convert from Midi to Tuneshare on Turbowarp.


 # Instructions

- Download everything as a ZIP.
- Open in a new tab the page https://onlinesequencer.net/ or other source 
- Load a MIDI file in the tab opened, select all the notes and click "copy".
- Go to the Input folder, create a new text file, paste the clipboard and save it.
- Do this for however many songs you like.
- Before running the `Converter.py` file, change the `"tempo"` argument in line 60 to the tempo of the song  or it will default to 110 and you can always change tempo in Native Tuneshare as well.
- Run the project and all the files in the Input folder will be converted and new text files will be created in the Output folder with the same rootless name e.g. input --> Example.txt ouput--> Example_converted.txt .
- Open that file, select all and copy it (press crtl+A and the crtl+C).
- Open CodeGIO's TuneShare project, log in, create a new tune and import the code you copied.
# NOTE: 
After running the converter you will either get a success message  `Converstion was successful and is saved as Example_converted.txt is the Output folder.` or a partial success `Converstion was partially successful with X missed notes and is saved as Example_converted.txt is the Output folder.` and if their is a Fatal Error it will give this message "Fatal Error {ErrorMessage}"

# Credits

- Big thanks to https://scratch.mit.edu/users/nerdboy628/ for creating the first fully working MIDI-to-TuneShare converter and for providing the necessary assets (basically the whole Assets folder was created by them). Their project can be found either at https://scratch.mit.edu/projects/870613190/ or https://snap.berkeley.edu/project?username=nerdboy628&projectname=MIDI%20to%20TuneShare%20Converter

- Also this project (converter.py file) was created by Gtl123 (https://scratch.mit.edu/users/Gtl123/ or https://replit.com/@GShukla19) and feel free to go and listen to his creations:)
