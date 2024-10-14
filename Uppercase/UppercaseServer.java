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

            String message = in.readLine();  // Receive message from client
            System.out.println("Received: " + message);

            String upperCaseMessage = message.toUpperCase();  // Convert to uppercase
            out.println(upperCaseMessage);  // Send back to client

            clientSocket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
