package com.conference.assistant.springboot.conferenceassistantspringboot.domain.user;

import org.junit.After;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.List;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;

@RunWith(SpringRunner.class)
@SpringBootTest
public class UserRepositoryTest {

    @Autowired
    UserRepository userRepository;

    @After
    public void cleanup(){
        userRepository.deleteAll();
    }

    @Test
    public void 회원저장_불러오기(){
        //given
        String email="test@naver.com";
        String name="test";
        String picture="http://picture.com";
        Status s = Status.VALID;

        // insert / update 수행
        userRepository.save(User.builder()
                    .email(email)
                    .name(name)
                    .picture(picture)
                    .status(s)
                    .build());
        //when
        List<User> userList = userRepository.findAll();

        //then
        User users = userList.get(0);
        assertThat(users.getEmail()).isEqualTo(email);
        assertThat(users.getName()).isEqualTo(name);
        assertThat(users.getPicture()).isEqualTo(picture);
        assertThat(users.getStatus()).isEqualTo(s);
    }
}