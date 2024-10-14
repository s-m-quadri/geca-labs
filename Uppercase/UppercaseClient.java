import java.io.*;
import java.net.*;

public class UppercaseClient {
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("localhost", 9090);

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            String message = "hello server";
            out.println(message); // Send message to server
            String response = in.readLine(); // Receive response from server

            System.out.println("Server response: " + response); // Output uppercase response

            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
