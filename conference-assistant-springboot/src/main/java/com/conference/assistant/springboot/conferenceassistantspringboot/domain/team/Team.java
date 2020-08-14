package com.conference.assistant.springboot.conferenceassistantspringboot.domain.team;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.User;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@NoArgsConstructor
@Getter
@Table(name="Team")
public class Team {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="team_id")
    private Long id;

    @Column(nullable = false, name="team_name")
    private String name;

    @Column(nullable = false)
    @Enumerated(EnumType.STRING)
    private Status_t status_t;

    @Column(nullable = false, name = "invite_url")
    private String invite;

    // 주인은 user의 team (@JoinColumn이 없다.)
    @OneToMany(mappedBy = "team")
    private List<User> users = new ArrayList<User>();

    @Builder
    public Team(String name, Status_t status_t, String invite, List<User> users) {
        this.name = name;
        this.status_t = status_t;
        this.invite = invite;
        this.users = users;
    }
}
