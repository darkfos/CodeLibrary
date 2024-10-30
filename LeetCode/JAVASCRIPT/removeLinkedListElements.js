
function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
}

let createListNode = (array) => {
    if (array.length >= 1) {
        var newHead = new ListNode(array[0]);
        let copyHead = newHead;

        for (let el = 1; el < array.length; el++) {
            copyHead.next = new ListNode(array[el]);
            copyHead = copyHead.next;
        }
    } else {
        return null
    }

    return newHead;
}

/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    /*
        EASY
        Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
    */
    
    let allElements = [];
    while (head) {
        let value = head.val;
        allElements.push(value);
        head = head.next;
    };
    allElements = allElements.filter((el) => el !== val);
    let newNode = createListNode(array=allElements);
    return newNode
};