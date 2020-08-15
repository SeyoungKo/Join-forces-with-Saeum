package com.conference.assistant.springboot.conferenceassistantspringboot.domain.team;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.User;
import org.junit.After;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;

import static org.assertj.core.api.AssertionsForInterfaceTypes.assertThat;

@RunWith(SpringRunner.class)
@SpringBootTest
public class TeamRepositoryTest {

    @Autowired
    TeamRepository teamRepository;

    @After
    public void cleanup(){
        teamRepository.deleteAll();
    }

    @Test
    @Transactional
    public void 팀저장_불러오기(){
        //given
        String name = "team1";
        Status status = Status.VALID;
        String invite = "http://invite_url.com";

        User user = new User();
        user.setName("team에서 호출한 user");
        user.setEmail("team에서 호출한 email");
        user.setPicture("team에서 호출한 picture");
        user.setStatus(com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.Status.VALID);

        List<User> userList = new ArrayList<User>();
        userList.add(user);

        // insert / update 수행
        teamRepository.save(Team.builder()
                .name(name)
                .status(status)
                .invite(invite)
                .users(userList)
                .build());

        //when
        List<Team> teamList = teamRepository.findAll();

        //then
        Team teams = teamList.get(0);
        assertThat(teams.getName()).isEqualTo(name);
        assertThat(teams.getStatus()).isEqualTo(status);
        assertThat(teams.getInvite()).isEqualTo(invite);
        assertThat(teams.getUsers().get(0).getEmail()).isEqualTo(user.getEmail());
    }
}