import java.net.*;
import java.io.*;

class GreetingClient {
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
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}

class GreetingServer {
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
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}

class UDPClient {
    public static void main(String[] args) {
        try {
            // Create a DatagramSocket
            DatagramSocket socket = new DatagramSocket();

            // Send message to server
            String message = "Hello UDP Server";
            byte[] sendBuffer = message.getBytes();
            InetAddress serverAddress = InetAddress.getByName("localhost");
            DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, serverAddress, 9876);
            socket.send(sendPacket);

            // Receive response from server
            byte[] receiveBuffer = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
            socket.receive(receivePacket); // Blocks until a message is received

            // Convert received data to string and print
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Server response: " + response);

            // Close socket
            socket.close();
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}

class UDPServer {
    public static void main(String[] args) {
        try {
            DatagramSocket socket = new DatagramSocket(9876);
            byte[] receiveBuffer = new byte[1024];

            System.out.println("Server is running, waiting for messages...");
            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket); // Receives client message
                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received from client: " + message);

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                DatagramPacket sendPacket = new DatagramPacket(message.getBytes(), message.length(), clientAddress,
                        clientPort);
                socket.send(sendPacket); // Sends the same message back
            }
        } catch (Exception e) {
            System.out.println("Something went wrong!");
        } finally {
            System.out.println("Connection Closed.");
        }
    }
}