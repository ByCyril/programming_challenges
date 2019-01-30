
public class Main {

	public static void main(String[] args) {

		LinkedList list = new LinkedList();

		int[] nums = {0,1,2,3,4,5,6,7,8,9};
		list.insertItems(nums);

		int size = list.size();
		list.printAll();

		System.out.println(size);
		
	}
}