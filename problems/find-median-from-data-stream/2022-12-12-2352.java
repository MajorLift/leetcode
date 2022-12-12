// Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/
// Accepted 2022-12-12 23:52 UTC · Java · 250 ms · 125.3 MB

class MedianFinder {
    private Queue<Integer> minHeap;
    private Queue<Integer> maxHeap;

    public MedianFinder() {
        this.minHeap = new PriorityQueue<>((a, b) -> a - b);
        this.maxHeap = new PriorityQueue<>((a, b) -> b - a);
    }
    
    public void addNum(int num) {
        if (this.minHeap.size() > this.maxHeap.size()) {
            this.minHeap.add(num);
            this.maxHeap.add(this.minHeap.poll());
        } else {
            this.maxHeap.add(num);
            this.minHeap.add(this.maxHeap.poll());
        }
    }
    
    public double findMedian() {
        if (this.minHeap.size() == this.maxHeap.size()) return (this.minHeap.peek() + this.maxHeap.peek()) / 2.0;
        return this.minHeap.peek() * 1.0;
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
