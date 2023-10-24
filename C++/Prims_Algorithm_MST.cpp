// Time Complexity -> O(E * log(E))
// Space Complexity -> O(E)

#include <bits/stdc++.h> 
vector<pair<pair<int, int>, int>> calculatePrimsMST(int n, int m, vector<pair<pair<int, int>, int>> &g)
{
    // Write your code here.

    vector<pair<int,int>> adj[n+1];

    for(auto& itr : g)
    {
        int u = itr.first.first;
        int v = itr.first.second;
        int wt = itr.second;

        adj[u].push_back({v, wt});
        adj[v].push_back({u, wt});
    }

    vector<pair<pair<int,int>, int>> ans;

    priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>> , greater<tuple<int,int,int>> > pq;

    pq.push(make_tuple(0, 1, -1));

    vector<bool> visited(n+1, false);

    int mstWt = 0;

    while(!pq.empty())
    {
        auto curr = pq.top();
        pq.pop();

        int wt = get<0>(curr);
        int node = get<1>(curr);
        int par = get<2>(curr);

        if(visited[node])
            continue;
        
        mstWt += wt;

        if(par != -1)
          ans.push_back({{par, node}, wt});

        visited[node] = true;

        for(auto& itr : adj[node])
        {
            int childNode = itr.first;
            int childWt = itr.second;

            if(!visited[childNode])
            {
                pq.push(make_tuple(childWt, childNode, node));
            }
        }
    }

    return ans;
}
