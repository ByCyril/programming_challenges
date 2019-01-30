
public class Main {

	public static void main(String[] args) {

		LinkedList list = new LinkedList();

		int[] nums = {0,1,2,3,4,5,6,7,8,9};
		list.insertItems(nums);

		System.out.println("All elements");
		list.printAll();

		System.out.println("All elements in reverse");
		list.printInReverse();

		System.out.println("Front and Back Elements");
		int front = list.seeFront();
		int back = list.seeBack();

		System.out.println(front);
		System.out.println(back);
		
	}
}