/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java_gui;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;


// Sends data from GUI to Python Controller
public class Client {

    private static Socket socket;
    private final String host = "localhost";
  
    //Port for sending data to Python controller
    private final int port = 65431;

    InetAddress address;
    OutputStream os;
    OutputStreamWriter osw;
    BufferedWriter bw;
    
    ////////////////////////// COMMANDS (TO PYTHON SERVER) //////////////////////////
    
    // Installation
    public final String installMT4  = "installMT4-";
    public final String installMT5  = "installMT5-";
    
    // Synchronization of files
    public final String syncMT4     = "syncMT4-";
    public final String syncMT5     = "syncMT5-";
    
    // For launching Strategy Tester
    public final String launchStrategyTester = "launchStrategyTester-";
 

    

    public Client() {

    }

    public void connectToServer() {
        try {
            address = InetAddress.getByName(host);
            socket = new Socket(address, port);

            //Send the message to the server
            os = socket.getOutputStream();
            osw = new OutputStreamWriter(os);
            bw = new BufferedWriter(osw);

        } catch (Exception exception) {
            exception.printStackTrace();
        }

    }

    public void sendMessage(String messageToPython) {

        try {
            bw.write(messageToPython);
            bw.flush();
        } catch (IOException ex) {
            Logger.getLogger(Client.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void closeSocket() {
        //Closing the socket
        try {
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}


/*
    // Java<=>Python Protocol: "header-data|data2|data3...|dataN"
    ////////////////////////// HEADER (TO PYTHON SERVER) //////////////////////////
    
    // Installation (Only header)
    "installMT4-"
    "installMT5-";
    
    // Synchronization of files (Only header)
    "syncMT4-"
    "syncMT5-"
 




*/