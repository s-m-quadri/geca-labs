import java.net.*;

public class UDPServer {
    public static void main(String[] args) {
        try {
            DatagramSocket socket = new DatagramSocket(9876);
            byte[] receiveBuffer = new byte[1024];

            System.out.println("Server is running, waiting for messages...");
            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);  // Receives client message
                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Received from client: " + message);

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                DatagramPacket sendPacket = new DatagramPacket(message.getBytes(), message.length(), clientAddress, clientPort);
                socket.send(sendPacket);  // Sends the same message back
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}