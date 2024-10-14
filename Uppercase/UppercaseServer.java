import java.io.*;
import java.net.*;

public class UppercaseServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(9090);
            System.out.println("Server waiting for client connection...");
            
            Socket clientSocket = serverSocket.accept();
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            
            out.println("Greetings!");
            out.println("Server v1.0 | GECA Assignment");
            out.println("Updated: October, 2024");
            while (true) {
                // Receive message from client
                String message = in.readLine();
                System.out.println("Received: " + message);
                
                // Shutdown server, in case of empty message
                if (message.equals("")) break;

                // Send back to client
                out.println(message.toUpperCase());
            }

            clientSocket.close();
            serverSocket.close();
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}
