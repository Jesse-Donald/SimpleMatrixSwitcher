# SimpleMatrixSwitcher
A small web server used to simplify changing presets on a HDMI Matrix written in python using Flask

![alt text](https://www.radioparts.com.au/Images/ProductImages/64538600.jpg)

## Usage
It is reccomended to run the server using docker

```bash
docker build simplematrix:latest
```

When runnnng you must specify:
- MATRIX_IP ( e.g. 192.168.1.100 )
- CONTAINER_ADDRESS ( e.g. 192.168.1.20:8001 )
- SOURCE_LABELS as a json list with the keys 'name' and 'icon'. It uses Google’s mdi icons. You can see the full searchable list of available icons [here](https://fonts.google.com/icons). An example is:
```json
SOURCE_LABELS='[{"name":"Computer","icon":"monitor"},{"name":"Laptop","icon":"laptop"},]]'
```
 
## Examples:
Running with podman run:
```bash
podman run -d -p 8001:8000 --name simplematrix -e MATRIX_IP="192.168.1.100" -e CONTAINER_ADDRESS="192.168.1.20:8001" -e SOURCE_LABELS='[{"name":"PC","icon":"monitor"}]' localhost/simplematrix:1.0
```
<img width="1084" height="888" alt="image" src="https://github.com/user-attachments/assets/e6efcfe4-28b8-4b57-9c17-4f8d4a31c7c5" />

### Planned Features
- [ ] Add dark mode toggle
  - [ ] Password Protect admin source

### Completed
- [x] Allow specifying ip adresses via envionmemt variables
- [x] Add advanced mode for further customization
- [x] Allow source labels and icons to be customised via environmennt vars
