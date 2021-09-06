#include <map>
#include <iostream>
#include <string>
#include <thread>
using namespace  std;

void f3()
{
	char * p = "f3 function";
}

void f2()
{
	char * p = "f2 function";
	f3();
}

void f1()
{
	long arr[100] = {0};
	for(long i = 0;i < 100; ++i)
	{
		arr[i] = i;
	}
	char * p = "f1 function";
	f2();
}

int main() {


    //std::thread thread = []{cout << "hello world " << endl;};
    std::thread thread([]{cout << "hello world " << endl;});
    thread.join();

    std::map<string, string> lm;
    lm["good"] = "heart";
	f1();
    // 查看map 里面内容
    //     std::cout<<lm["good"];
}
