

public class LinkedList {

	private Node head;
	private Node tail;
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
			Node newNode = new Node(id);
			newNode.prev = currentHead;
			currentHead.next = newNode;
			currentHead = newNode;
			tail = newNode;
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

	public int seeFront() {
		return head.id;
	}

	public int seeBack() {
		return tail.id;
	}

	public void printInReverse() {
		Node currentHead = tail;
		while (currentHead.prev != null) {
			System.out.println(currentHead.id);
			currentHead = currentHead.prev;
		}
		System.out.println(currentHead.id);
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









