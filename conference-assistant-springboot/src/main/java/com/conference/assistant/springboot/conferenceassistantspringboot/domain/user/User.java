package com.conference.assistant.springboot.conferenceassistantspringboot.domain.user;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Getter
@NoArgsConstructor
@Entity
@Table(name="User")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="user_id") // 연관관계 매핑 (affiliation)
    private Long id;

    @Column(nullable = false)
    private String email;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String picture;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Role role;

    // User.team이 연관관계의 주인 (등록, 수정 o- 다수인 쪽이 주인)
    @ManyToOne
    @JoinColumn(name="team_id")
    private Team team;

    @Builder
    public User(String email, String name, String picture, Role role, Team team) {
        this.email = email;
        this.name = name;
        this.picture = picture;
        this.role = role;
        this.team = team;
    }

    public User update(String name, String picture){
        this.name = name;
        this.picture = picture;
        return this;
    }
}
