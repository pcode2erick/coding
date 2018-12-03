import java.io.*;
import java.net.*;

class UDPClient
{
	static int inventory=1000;
   public static void main(String args[]) throws Exception
   {
	  int item=0;
      BufferedReader inFromUser =
         new BufferedReader(new InputStreamReader(System.in));
      DatagramSocket clientSocket = new DatagramSocket();
      InetAddress IPAddress = InetAddress.getByName("192.168.0.101");
	   while(true){
      byte[] sendData = new byte[1024];
      byte[] receiveData = new byte[1024];
	  
      String sentence = inFromUser.readLine();
	  String []str=new String[2];
	  str=sentence.split(" ");
	  str[0]=str[0].toUpperCase();
	  if(str[0].equals("SEND")){
		  item=Integer.parseInt(str[1]);
		  inventory-=item;
		 System.out.println("SEND PROCESS:"+str[1]+" item(s)");
	  }
      sendData = sentence.getBytes();
      DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
      clientSocket.send(sendPacket);
      DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
      clientSocket.receive(receivePacket);
      String modifiedSentence = new String(receivePacket.getData());
      System.out.println("FROM SERVER:" + modifiedSentence);
      //clientSocket.close();
   }
   }
}