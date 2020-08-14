package com.conference.assistant.springboot.conferenceassistantspringboot.domain.room;

import com.conference.assistant.springboot.conferenceassistantspringboot.domain.team.Team;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import javax.persistence.*;

@Getter
@NoArgsConstructor
@Entity
public class Room {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(nullable = false, name="room_id")
    private Long id;

    @Column(nullable = false, name="room_name")
    private String name;

    @Column(nullable = false)
    @Enumerated(EnumType.STRING)
    private Status_r status_r;

    // team id 참조
    @ManyToOne
    @JoinColumn(name="team_id")
    private Team team;

    @Builder
    public Room(String name, Status_r status_r, Team team) {
        this.name = name;
        this.status_r = status_r;
        this.team = team;
    }
}
