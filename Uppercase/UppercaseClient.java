import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UppercaseClient {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(System.in);
            Socket socket = new Socket("localhost", 9090);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            // Three line header from server
            System.out.println(in.readLine());
            System.out.println(in.readLine());
            System.out.println(in.readLine());

            while (true) {
                // Send message to server
                System.out.print("send ➜ ");
                String message = scanner.nextLine();
                out.println(message);

                // In case of empty message, server will shutdown
                // and so do the client prompt
                if (message.equals(""))
                    break;

                // Get response
                String response = in.readLine();
                System.out.println(response);
            }

            socket.close();
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}
