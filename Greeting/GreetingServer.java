import java.io.*;
import java.net.*;

public class GreetingServer {
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(8080);
            System.out.println("Server is waiting for a client...");

            Socket socket = serverSocket.accept(); // Accepts client connection
            System.out.println("Client connected!");

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            out.println("Hello, Client!");

            socket.close();
            serverSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
