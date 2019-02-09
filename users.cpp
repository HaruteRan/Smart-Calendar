//
//  users.cpp
//  Smart Calendar DS
//
//  Created by apple on 1/29/19.
//  Copyright © 2019 apple. All rights reserved.
//

#include "users.hpp"

void timeslot::print(){
    if (day == 1) cout << "Monday ";
    if (day == 2) cout << "Tuesday ";
    if (day == 3) cout << "Wednesday ";
    if (day == 4) cout << "Thursday ";
    if (day == 5) cout << "Friday ";
    if (day == 6) cout << "Saturday ";
    if (day == 7) cout << "Sunday ";
    cout << "from " << setw(2) << setfill('0')<< s_t/100 << ":" <<setw(2) << setfill('0')<< s_t%100;
    if (s_t/100 < 12) cout << " am ";
    else cout << " pm ";
    cout << "to " << setw(2) << setfill('0') << e_t/100 << ":" << setw(2) << setfill('0')<< e_t%100;
    if (e_t/100 < 12) cout << " am ";
    else cout << " pm ";
    cout << endl;
}

void user::c_register(course a_course){
    courses.push_back(a_course);
    a_course.add_classmate(*this);
}

void user::print_sch(){
    cout << user_name << "'s schedule:" << endl;
    for (int i = 0; i < courses.size(); i ++){
        courses[i].print();
    }
}

void course::print(){
    for (int i = 0; i < time.size(); i++){
        cout << c_nm << " by Professor " << i_nm << ". ";
        time[i].print();
    }
}
