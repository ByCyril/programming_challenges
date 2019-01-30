

public class LinkedList {

	private Node head;
	private int size;;

	public void insert(int id) {
		Node currentHead = head;

		if (currentHead == null) {
			head = new Node(id);
			currentHead = head;
			size += 1;
		} else {
			while (currentHead.next != null) {
				currentHead = currentHead.next;
			}
			currentHead.next = new Node(id);
			size += 1;
		}
	}

	public void delete(int index) {

		Node currentHead = head;
		int i = 0;

		while (i < index - 1) {
			if (currentHead.next != null) {
				currentHead = currentHead.next;
				i += 1;
			}
		}

		currentHead.next = currentHead.next.next;
		size -= 1;
	}

	public void insertItems(int[] nums) {
		for (int i = 0; i < nums.length; i++) {
			int num = nums[i];
			insert(num);
		}
	}

	public int size() {
		return this.size;
	}

	public void printAll() {
		Node currentHead = head;

		while (currentHead.next != null) {
			System.out.println(currentHead.id);
			currentHead = currentHead.next;
		}

		System.out.println(currentHead.id);
	}
}









