package com.conference.assistant.springboot.conferenceassistantspringboot.domain.team;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.BaseTimeEntity;
import com.conference.assistant.springboot.conferenceassistantspringboot.domain.user.User;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@NoArgsConstructor
@Getter
@Entity
@Table(name="team")
public class Team extends BaseTimeEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="team_id")
    private Long id;

    @Column(nullable = false, name="team_name")
    private String name;

    @Column(nullable = false, name="status_team")
    @Enumerated(EnumType.STRING)
    private Status status;

    @Column(nullable = false, name = "invite_url")
    private String invite;

    // 주인은 user의 team (@JoinColumn이 없다.)
    @OneToMany(mappedBy = "team")
    private List<User> users = new ArrayList<User>();

    @Builder
    public Team(String name, Status status, String invite, List<User> users) {
        this.name = name;
        this.status = status;
        this.invite = invite;
        this.users = users;
    }
}
