//
//  main.cpp
//  Smart Calendar DS
//
//  Created by apple on 1/21/19.
//  Copyright © 2019 apple. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <unordered_set>

#include "users.hpp"

typedef unordered_set<user> users;

int main() {
    // here we input users
    user LZY(1000, "Li Zhengyu", "I am the king of the world!");
    user WYS(1000, "Wen Yunshi", "Nothing is true, everything is permitted");
    user LSJ(1000, "Li Shengjin", "To be or not to be, that is a question");
    
    // here we input some courses
    // first set up some timeslots
    timeslot a = timeslot(1, 1200, 1400);
    timeslot b = timeslot(4, 1200, 1400);
    timeslot c = timeslot(2, 1330, 1530);
    timeslot d = timeslot(5, 1700, 1900);
    timeslot e = timeslot(3, 800, 1000);
    // then set up some combinations
    vector<timeslot> A = {a,b};
    vector<timeslot> B = {c,d};
    vector<timeslot> C = {b,d,e};
    // then set some some courses
    course ds = course("Data Structures", "Babara Cutler", A);
    course focs = course("Foundation of Computer Science", "Stacey Patterson", B);
    course co = course("Computer Organization", "George Slota", C);
    
    // let students register for classes
    LZY.c_register(ds);
    LZY.c_register(focs);
    LZY.c_register(co);
    WYS.c_register(focs);
    WYS.c_register(co);
    LSJ.c_register(ds);
    LSJ.c_register(co);
    
    // print schedule
    LZY.print_sch();
    WYS.print_sch();
    LSJ.print_sch();
    
    return 0;
}
