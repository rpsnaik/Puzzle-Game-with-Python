const electron = require('electron');
const url = require('url');
const path = require('path');
const {app, BrowserWindow, Menu} = electron;
let mainWindow;
let addWindow;
app.on('ready', function(){
    mainWindow = new BrowserWindow({});
    mainWindow.loadURL(url.format({
        pathname:path.join(__dirname, 'index.html'),
        protocol:'file',
        slashes:true
    }));
    mainWindow.on('closed', function(){
        app.quit();
    })

});





 