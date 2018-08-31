

class ImplementingLinkedList {

    static class  Node
    { 
         int data; 
         Node next;  
        Node prve; 
       
       public  Node (int data)
        {
           this.data  = data ; 
       }
   }  

     
       Node head; 
     
    public  void insert(Node node) 
     
       {
        if (head == null)
        head = node;  
        else {
            Node newNode = head; 
            while (newNode.next  != null )
             {
                newNode = newNode.next; 
              }
               newNode.next  = node; 
        } 
        
    } 
    
    public  void  insertAtStart(Node node) 
        {
        node.next = head;
        head = node;     
        }
    
    public void printList()
    {
        Node node = head;  
        while (node != null ) 
        {
         System.out.println(node.data);
        node   = node.next ;  
        }
    } 
    
     public void insertAtIndex(int index , Node node)
      {   
     if (index  == 0) {
         insertAtStart(node); 
     } else {
         Node newNode  = head; 
         for( int startIndex = 0; startIndex   <  index - 1; startIndex  ++)  
         {
             newNode   = newNode.next;
            
         }
          node.next = newNode.next; // copy the addrass of the node at this point and past it at the newNode .
          newNode.next = node;   
     }    
         
     }
    
    public  void removeAtStart() {
        head = head.next; 
    }
    
    public static void main(String[] args) 
        {
       ImplementingLinkedList list = new ImplementingLinkedList();
       list.insertAtStart(new Node(100));
         list.insert(new Node(200));
         list.insert(new Node(300));
         list.insert(new Node (400));
         list.insert(new Node(500));
         list.insertAtIndex(3, new Node(600));
         list.removeAtStart();
        list.printList();          
    }
    
    
}
