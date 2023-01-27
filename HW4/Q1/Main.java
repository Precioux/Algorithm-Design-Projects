/*
Samin Mahdipour - 9839039
Algorithm Design - HW4 - Q1
*/
import java.io.*;
import java.util.*;
public class Main {

	static class Node implements Comparator<Node> {

		public int node;
		public int cost;

		public Node() {}

		public Node(int node, int cost)
		{
			this.node = node;
			this.cost = cost;
		}

		@Override
		public int compare(Node node1, Node node2)
		{
			if (node1.cost < node2.cost)
				return -1;
			if (node1.cost > node2.cost)
				return 1;
			return 0;
		}
	}


	static void createE(ArrayList<ArrayList<Node> > graph,
						int x, int y, int w)
	{
		graph.get(x).add(new Node(y, w));
		graph.get(y).add(new Node(x, w));
	}


	static void dijkstraAlgo(ArrayList<ArrayList<Node> > graph,
						int src, int n, int dFrom0[],
						int numPath[])
	{

		PriorityQueue<Node> priorotyQ
			= new PriorityQueue<Node>(n + 1, new Node());

		Set<String> checked = new HashSet<String>();

		priorotyQ.add(new Node(src, 0));

		dFrom0[src] = 0;
		numPath[src] = 1;

		while (!priorotyQ.isEmpty()) {

			int u = priorotyQ.peek().node;

			int d = priorotyQ.peek().cost;

			priorotyQ.poll();

			for (int i = 0; i < graph.get(u).size(); i++) {
				int to = graph.get(u).get(i).node;
				int cost = graph.get(u).get(i).cost;

				if (checked.contains(to + " " + u))
					continue;

				if (dFrom0[to] > dFrom0[u] + cost) {

					priorotyQ.add(new Node(to, d + cost));

					dFrom0[to] = dFrom0[u] + cost;

					numPath[to] = numPath[u];
				}

				else if (dFrom0[to] == dFrom0[u] + cost) {
					numPath[to] = (numPath[to] + numPath[u]);
				}

				checked.add(to + " " + u);
			}
		}
	}

	static int
	numShortPaths(ArrayList<ArrayList<Node> > graph,
					int s, int n)
	{

		int[] dFrom0 = new int[n + 5];
		int[] numPath = new int[n + 5];

		for (int i = 0; i <= n; i++)
			dFrom0[i] = Integer.MAX_VALUE;

		for (int i = 0; i <= n; i++)
			numPath[i] = 0;

		dijkstraAlgo(graph, s, n, dFrom0, numPath);
        return numPath[n];
	}
	

	public static void main(String[] args)
	{
	    Scanner scanner = new Scanner(System.in);
		int N = scanner.nextInt();
		int M = scanner.nextInt();

		ArrayList<ArrayList<Node> > graph = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			graph.add(new ArrayList<Node>());
		}
		
		for(int i=0;i<M;i++){
		    int startV = scanner.nextInt();
		    int endV = scanner.nextInt();
		    int w = scanner.nextInt();
		    createE(graph,startV,endV,w);
		}

		int result = numShortPaths(graph, 0, N-1);
		System.out.print(result);
	}
}
