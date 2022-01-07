## FTP 

- FTP server uses UNIX accounts for authentication. Root credentials can be found in `Dockerfile`.
  - The root credentials are very weak and can easily be guessed.
  - `ftp -p localhost`
- `notes` folder in FTP directory contains clues to HTTP server credentials
  - `note.txt` is signed `jeff` -- this is the HTTP server username.
  - `pwds.txt` contains a list of previously used passwords. The same base password is used each year. One can infer that the current password may follow the pattern and thus be `i_like_c0ff33_2021`.
  - Logging in at [http://localhost/](http://localhost/) will reveal the key.

SC3{Y0u_founD_m3_m@t3!}
