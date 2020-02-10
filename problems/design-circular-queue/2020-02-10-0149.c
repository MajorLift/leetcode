// Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/
// Accepted 2020-02-10 01:49 UTC · C · 20 ms · 13.8 MB




typedef struct {
    int* array;
    int head;
    int tail;
    int size;
    int curr_size;
} MyCircularQueue;

/** Initialize your data structure here. Set the size of the queue to be k. */

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue* queue = (MyCircularQueue*) malloc(sizeof(MyCircularQueue));
    queue->array = (int*) malloc(sizeof(int) * k);
    queue->head = 0;
    queue->tail = k - 1;
    queue->size = k;
    queue->curr_size = 0;
    return queue;
}

/** Checks whether the circular queue is empty or not. */
bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    return obj->curr_size <= 0;
}

/** Checks whether the circular queue is full or not. */
bool myCircularQueueIsFull(MyCircularQueue* obj) {
    return obj->curr_size >= obj->size;
}

/** Insert an element into the circular queue. Return true if the operation is successful. */
bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if(myCircularQueueIsFull(obj)){
        return false;
    }
    // if(myCircularQueueIsEmpty(obj)){
    //     obj->head = 0;
    //     obj->tail = 0;
    // }
    obj->tail = (obj->tail + 1) % obj->size;
    obj->array[obj->tail] = value;
    obj->curr_size += 1;
    return true;
}

/** Delete an element from the circular queue. Return true if the operation is successful. */
bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if(myCircularQueueIsEmpty(obj)){
        return false;
    }
    obj->head = (obj->head + 1) % obj->size;
    obj->curr_size -= 1;
    return true;
}

/** Get the front item from the queue. */
int myCircularQueueFront(MyCircularQueue* obj) {
    if(myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->array[obj->head];
}

/** Get the last item from the queue. */
int myCircularQueueRear(MyCircularQueue* obj) {
    if(myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->array[obj->tail];
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->array);
    free(obj);
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/
