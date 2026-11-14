# SimpleMatrixSwitcher
A small web server used to simplify changing presets on a HDMI Matrix written in python using Flask

![alt text](https://www.radioparts.com.au/Images/ProductImages/64538600.jpg)

It is reccomended to run the server using docker

```bash
docker build simplematrix:latest
```

When runnnng specify the matrix and dockwr host details

```bash
podman run -d -p 8001:8000 --name simplematrix -e MATRIX_IP="192.168.1.50" -e CONTAINER_ADDRESS="10.40.5.60:8001" localhost/simplematrix:latest
```
### Planned Features
- [ ] Add dark mode toggle
- [ ] Allow dashboard customisation via environment variables
  - [ ] Password Protect admin source

### Completed
- [x] Allow specifying ip adresses via envionmemt variables
- [x] Add advances mode for further customization
