import java.io.*;
import java.net.*;

public class GreetingClient {
    public static void main(String[] args) {
        try {
            // Connect to the server at localhost on port 8080
            Socket socket = new Socket("localhost", 8080);
            
            // Create input stream to receive data from server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Read and print server message
            String serverMessage = in.readLine();
            System.out.println("Server says: " + serverMessage);

            // Close the connection
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
