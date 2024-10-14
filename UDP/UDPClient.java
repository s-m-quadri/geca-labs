import java.net.*;

public class UDPClient {
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
            socket.receive(receivePacket);  // Blocks until a message is received

            // Convert received data to string and print
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Server response: " + response);
            
            // Close socket
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
