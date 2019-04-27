#include<stdio.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
#define MAX 100
using namespace std;
struct point{
    int x;
    int y;
};
struct Q{
    struct point node[MAX];
    int front;    //队头
    int rear;     //队尾
    struct point p;
};
struct st{
    struct point n[20];
    int top;    //栈顶
};
int arr[10][10]={{0,0,0, 0, 0,  0,  0,  0,0,0},
                 {0,0,0, 0, 0,  0,  0,  0,0,0},
                 {0,0,0, 0, 0,  0,  0,  0,0,0},
                 {0,0,0,999,999,999,999,0,0,0},
                 {0,0,0,999,999,999,999,0,0,0},
                 {0,0,0,999,999,999,999,0,0,0},
                 {0,0,0,999,999,999,999,0,0,0},
                 {0,0,0, 0, 0,  0,  0,  0,0,0},
                 {0,0,0, 0, 0,  0,  0,  0,0,0},
                 {0,0,0, 0, 0,  0,  0,  0,0,0}};

//BFS标记              
int flag[10][10] = {0};

//DFS标记
int flag2[10][10]={{0,0,0,0,0,0,0,0,0,0},
                   {0,0,0,0,0,0,0,0,0,0},
                   {0,0,0,0,0,0,0,0,0,0},
                   {0,0,0,1,1,1,1,0,0,0},
                   {0,0,0,1,1,1,1,0,0,0},
                   {0,0,0,1,1,1,1,0,0,0},
                   {0,0,0,1,1,1,1,0,0,0},
                   {0,0,0,0,0,0,0,0,0,0},
                   {0,0,0,0,0,0,0,0,0,0},
                   {0,0,0,0,0,0,0,0,0,0}};

int a = 0;   //最短路径找到标志位
int t = 1;   //当前层数，即步数
bool f = false;
struct point current;  //小车当前的位置
struct point way[20];//标记路径
//初始化所有
void initall(){
    int i,j;
    a = 0;
    t = 1;
    f = false;
    for(i = 0;i<10;i++){
        for(j = 0;j<10;j++){
            flag[i][j] = 0;
            flag2[i][j] = 0;
        }
    }
    for(i = 3;i<7;i++){
        for(j = 3;j<7;j++){
            flag2[i][j] = 1;
        }
    }
    for(i = 0;i < 20;i++){
        way[i].x = 999;
        way[i].y = 999;
    }
}

//初始化队列
void initQueue(struct Q *que){
    que->rear = 0;
    que->front = 0;
}
//队列查空
int empty(struct Q *que){
    if(que->rear <= que->front)
        return 1;
    else
        return 0;
}
//入队
void enterQueue(struct Q *que,struct point *pin){
    que->node[que->rear].x = pin->x;
    que->node[que->rear].y = pin->y;
    que->rear += 1;
    flag[pin->x][pin->y] = 1;
}

//出队
struct point deletQueue(struct Q *que){ 
    struct point pin = que->node[que->front];
    que->front += 1;
    return pin;
}
void BFS(int ax,int ay){
    int num = 1;   //记录当前层数的结点个数，初始化为第一层
    int a[20];     //记录各层结点数
    struct Q queue,*que;
    struct point p,cur,*pin;
    pin = &p;
    pin->x = current.x;
    pin->y = current.y;
    // cout << "curx" <<pin->x <<endl;
    // cout << "cury" <<pin->y <<endl;
    que = &queue;
    initQueue(que);
    enterQueue(que,pin);
    a[t] = num; 
    while(!empty(que)){
        num = 0;
        while(a[t]>0){  
            cur = deletQueue(que);
            if((cur.x-1)>= 0 && (cur.x-1)<10 && !flag[(cur.x)-1][cur.y] && arr[cur.x-1][cur.y] != 999){
                num++;
                pin->x = cur.x-1;
                pin->y = cur.y;
                if(cur.x-1 == ax && cur.y == ay)
                    return;
                enterQueue(que,pin);
            }
            if((cur.y-1)>= 0 && (cur.y-1)<10 && !flag[cur.x][(cur.y)-1] && arr[cur.x][cur.y-1] != 999){
                num++;
                pin->x = cur.x;
                pin->y = cur.y-1;
                if(cur.x == ax && cur.y-1 == ay)
                    return;
                enterQueue(que,pin);
            }
            if((cur.x+1)>= 0 && (cur.x+1)< 10 && !flag[(cur.x)+1][cur.y] && arr[cur.x+1][cur.y] != 999){
                num++;
                pin->x = cur.x+1;
                pin->y = cur.y;
                if(cur.x+1 == ax && cur.y == ay)
                    return;
                enterQueue(que,pin);
            }
            if((cur.y+1)>= 0 && (cur.y+1)< 10 && !flag[cur.x][cur.y+1] && arr[cur.x][cur.y+1] != 999 ){
                num++;
                pin->x = cur.x;
                pin->y = cur.y+1;
                if(cur.x == ax && cur.y+1 == ay)
                    return;
                enterQueue(que,pin);
            }
            a[t]--;
        }
        t++;
        if(f)
            return;
        a[t]=num;
    }
}

//初始化栈
void init(struct st *s){

    s->top = -1;    
}
//栈查空
int empty(struct st *s){
    if(s->top == -1)
        return 1;
    else
        return 0;
}
//入栈
void push(struct st *s,struct point p){
    s->top ++;
    s->n[s->top].x = p.x;
    s->n[s->top].y = p.y;
    flag2[s->n[s->top].x][s->n[s->top].y] = 1;
}
//出栈
int pop(struct st *s,struct point p){
    if(s->top == -1)
        return 0;
    else{
        flag2[s->n[s->top].x][s->n[s->top].y] = 0;
        s->top--;
        return 1;
    }
}
void DFS(struct st *s,struct point p,int ax,int ay){
    int k = 0;              //数组标志
    struct point w;         //递归函数传参
    int i;
    if(p.x<0 || p.y<0 || p.x>=10 || p.y>=10 || flag2[p.x][p.y] == 1){
        return;
    }
    if(p.x>=0 && p.y>=0 && p.x<10 && p.y<10 && flag2[p.x][p.y] == 0){
        push(s,p);
    }
    if(s->top == t &&(p.x!=ax || p.y!=ay) ){
        i = pop(s,p);
        return ;
    }
    if(s->top == t && p.x==ax && p.y==ay){
        a = 1;
        while((s->top)>= 0){
            way[k] = s->n[s->top];
            i = pop(s,p);
            k++;
        }
        return;
    }
    if(!a){
        w.x = p.x+1;
        w.y = p.y;
        DFS(s,w,ax,ay); 
    }
    if(!a){
        w.x = p.x;
        w.y = p.y+1;
        DFS(s,w,ax,ay);
    }
    if(!a){
        w.x = p.x;
        w.y = p.y-1;
        DFS(s, w,ax,ay);
    }
    if(!a){
        w.x = p.x-1;
        w.y = p.y;
        DFS(s,w,ax,ay);
    }
    pop(s,p);
}

//寻找最短路径走的方向
long find(struct point way[]){
    int j = 1;          //记录路径个数
    int i = 0;
    int r = 0;
    string p;
    char temp;
    while(i < t){
        while((way[i].x == way[i+1].x) && (way[i].y<way[i+1].y)){
            i++;
            r++;
        }
        if(r > 0){
            temp = 4 +'0'; 
            p += temp;    //e
            temp = r +'0';
            p += temp;
            r = 0;
        }
        while((way[i].x == way[i+1].x) && (way[i].y>way[i+1].y)){
            i++;
            r++;
        }   
        if(r > 0){
            temp = 2 +'0'; 
            p += temp;    //w
            temp = r +'0';
            p += temp;
            r = 0;
        }
        while((way[i].y == way[i+1].y) && (way[i].x<way[i+1].x)){
            i++;
            r++;
        }       
        if(r > 0){
            temp = 3 +'0'; 
            p += temp;    //s
            temp = r +'0';
            p += temp;
            r = 0;
        }
        while((way[i].y == way[i+1].y) && (way[i].x>way[i+1].x)){
            i++;
            r++;
        }       
        if(r > 0){
            temp = 1 +'0'; 
            p += temp;    //n
            temp = r +'0';
            p += temp;
            r = 0;
        }
    }   
    cout << p <<endl;
    long plan = atoi(p.c_str());
    return plan;
}


class TestLib  
{  
    public:   
        int test(int ax,int ay,int curx,int cury);
        long runway(int ax,int ay,int curx,int cury);  
};    
int TestLib::test(int ax,int ay,int curx,int cury) { 
    struct st stack;
    struct st *s;
    initall();
    current.x = curx;
    current.y = cury;
    // cout << "aimx" <<ax <<" aimy"<<ay<<endl;
    // cout << "curx" <<curx<<" cury"<<cury<<endl;
    // cout << "bfs start" << endl;
    BFS(ax,ay);
    // cout << "bfs over" << endl;
    cout << "root" <<t << endl;
    //cout << "ok" << endl;
    return t;
}  
long TestLib::runway(int ax,int ay,int curx,int cury) {  
    struct st stack;
    struct st *s;
    initall();
    current.x = curx;
    current.y = cury;
    // cout << "bfs start" << endl;
    BFS(ax,ay);
    // cout << "bfs over" << endl;
    cout << "root" <<t << endl;
    s = &stack;
    init(s);
    // cout << "dfs s" << endl;    
    DFS(s,current,ax,ay);
    // cout << "dfs o" << endl;

    reverse(way,way + t + 1);
    //cout << "root :" << endl;
    // for(int i = 0;i < t + 1;i++){
    //     cout << way[i].x << " " << way[i].y<< endl;
    // }
    for(int z = t+1;z < 20;z++){
        way[z].x = 999;
        way[z].y = 999;
    }
    long plan = find(way);
    // cout << "root = " << plan << endl;
    return plan;
}

extern "C" {  
    TestLib obj;   
    long display_int(int ax,int ay,int curx,int cury) {  
        obj.runway(ax,ay,curx,cury);   
      } 
    int display_string(int ax,int ay,int curx,int cury) {  
        obj.test(ax,ay,curx,cury);   
      }  
}  