# Colornote to Quillpad

A super simple script that converts a [Colornote](https://play.google.com/store/apps/details?id=com.socialnmobile.dictapps.notepad.color.note) sqlite database to a [Quillpad](https://quillpad.github.io/) backup. I had to make this for someone who was stuck on Colornote and wanted to switch to a different note taking app.

## Getting the Colornote SQLite database
Getting the sqlite database from Colornote is the tricky part. There are 2 ways:

### If your phone is rooted
- Download Total Commander, go to the root folder, and navigate to `/data/data/com.socialnmobile.dictapps.notepad.color.note/databases` and download the `colornote.db` file into your computer in the same folder as the python script

### If your phone is not rooted
- Backup colornotes
- Download and run an Android emulator on your pc, like [Bluestacks](https://www.bluestacks.com/)
- [Root the android emulator](https://appuals.com/root-bluestacks/) (It's very easy, you just switch a couple 0s to 1s in a text file)
- Follow the above steps in the [If your phone is rooted](#if-your-phone-is-rooted) section
- You can copy the file onto an accessible location like Downloads, and then use the bluestacks media manager to download it onto your computer
